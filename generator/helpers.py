from typing import Dict, Tuple

from django.forms.models import (
    model_to_dict,
)
from django.shortcuts import (
    get_object_or_404,
)

from .models import (
    Game, 
    Round, 
    Question, 
   # AnswerOptions,
)
from .serializer import(
    GameSerializer,
    RoundSerializer,
    QuestionSerializer,
  #  AnswerOptionsSerializer,
)


def get_one_game_with_rounds(request, *args, **kwargs) -> Dict:
    """Формирует словарь с информацией об игре и ее раундах."""

    game = Game.objects.prefetch_related('round_set').get(id=kwargs['pk'])
    rounds = game.round_set.all()
    rounds_list = []
    for _round in rounds:
        round_dict = model_to_dict(_round)
        questions = _round.question_set.values(
            'id', 
            'question_type',
            'question_text',
            'show_image',
            'image_before',
            'image_after',
            'video_before',
            'video_after',
            'image_after',
            'time_to_answer',
            'correct_answer',
            'answers',
            'player_displayed',
        )
        for question in questions:
            question['category_names'] = list(Question.objects.filter(id=question['id']).values_list('category__name', flat=True))
        round_dict['questions'] = list(questions)
        rounds_list.append(round_dict)

    game = model_to_dict(game)

    result = {
        **game,
        'rounds': list(rounds_list),
    }

    return result

def update_game_with_rounds(request, *args, **kwargs):
    game = get_object_or_404(Game, id=kwargs['pk'])
    game_serializer = GameSerializer(game, data=request.data)

    if game_serializer.is_valid():
        game_serializer.save()

        for round_data in request.data.get('rounds', []):
            round = game.round_set.get(id=round_data['id'])
            round_serializer = RoundSerializer(round, data=round_data)

            if round_serializer.is_valid():
                round_serializer.save()

                for question_data in round_data.get('questions', []):
                    question = round.question_set.get(id=question_data['id'])
                    question_serializer = QuestionSerializer(question, data=question_data)

                    if question_serializer.is_valid():
                        question_serializer.save()

                        answer = Question.objects.filter(quest_id_id=question['id']).get(answer=question_data)
                        #answer_serializer = AnswerOptionsSerializer(answer, data=question_data)

                        if answer_serializer.is_valid():
                            answer_serializer.save()
                        else:
                            return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(round_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(game_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_names_all_games() -> Dict:
    """Формирует словарь с информацией о всех играх.
    
    Конечный словарь не содержит информации о раундах, вопросах, ответах на вопросы и медиа.
    """

    return Game.objects.all().values(
        'id', 
        'name',
        'theme',
        'date',
    ).order_by(
        '-id',
    )


def get_game_for_json(request, *args, **kwargs) -> Tuple[Dict, str]:
    """Формирует словарь с информацией об игре и ее раундах.

    Конечный словарь не содержит информации о вопросах, ответах на вопросы и медиа.
    """

    game = Game.objects.get(id=kwargs['pk'])

    rounds = game.round_set.values(
        'id', 
        'name', 
        'round_type',
    )

    game = model_to_dict(game)

    result = {
        **game,
        'rounds': list(rounds),
    }

    return result, game['id']


def create_game(data) -> Tuple[Dict, bool]:

    rounds = data.get('game')['rounds']

    game = Game.objects.create(
        **data.get('game')['game_info'],
        **data.get('game')['game_settings']['tactics'],
        skip_emails=data.get('game')['game_settings']['skip_emails'],
    )

    for current_round in rounds:
        questions = current_round.pop('questions')
        _round = Round.objects.create(
            game_id=game,
            round_type=current_round['type'],
            **current_round['settings'],
        )

        for current_question in questions:
            answers = current_question.pop('answers')
            media_data = current_question['media_data']
            question = Question.objects.create(
                question_type=current_question['type'],
                question_text=current_question['question'],
                show_image=media_data['show_image'],
                image_before=media_data['video']['before'],
                image_after=media_data['video']['after'],
                video_before=media_data['image']['before'],
                video_after=media_data['image']['after'],
                time_to_answer=current_question['time_to_answer'],
            )
            question.round_id.add(_round)

            for answer in answers:
                AnswerOptions.objects.create(
                    quest_id=question,
                    answer=answer,
                    answer_is_correct=answer==current_question['correct_answer'],
                )

    return model_to_dict(game), True


def create_round(data):
    game = Game.objects.get(id=data['game_id'])
    _round = Round.objects.create(
        game_id=game,
        round_type=data['type'],
        **data['settings'],
    )

    questions = data.pop('questions')

    for current_question in questions:
        answers = current_question.pop('answers')
        media_data = current_question['media_data']
        question = Question.objects.create(
            question_type=current_question['type'],
            question_text=current_question['question'],
            show_image=media_data['show_image'],
            image_before=media_data['video']['before'],
            image_after=media_data['video']['after'],
            video_before=media_data['image']['before'],
            video_after=media_data['image']['after'],
            time_to_answer=current_question['time_to_answer'],
            answers=current_question['answers'],
            correct_answer=current_question['correct_answer']
        )

        question.round_id.add(_round)

        # for answer in answers:
        #     AnswerOptions.objects.create(
        #         quest_id=question,
        #         answer=answer,
        #         answer_is_correct=answer==current_question['correct_answer'],
        #     )

    return model_to_dict(_round), True


# def get_one_game_with_full_info(request, *args, **kwargs):
    
#     from django.db.models import Prefetch

#     game = Game.objects.prefetch_related('round_set').get(id=kwargs['pk'])
#     rounds = game.round_set.prefetch_related('question_set').filter(game_id=game)
#     questions = [_round.question_set.filter(round_id=_round) for _round in rounds]

#     game_info = {
#         'name': game.name,
#         'theme': game.theme,
#         'client': game.client,
#         'date': game.date,
#     }
#     game_settings_tactics = {
#         'remove_answer': game.remove_answer,
#         'one_for_all': game.one_for_all,
#         'question_bet': game.question_bet,
#         'all_in': game.all_in,
#         'team_bet': game.team_bet,
#     }
#     rounds = [
#         {
#             'type': '',
#             'settings': {
#                 'is_test': '',
#                 'name': '',
#                 'display_name': '',
#                 'time_to_answer': '',
#                 'use_special_tactics': '',
#             },
#             'questions': [
#                 {   
#                     'type': '',
#                     'question': '',
#                     'answers': [

#                     ],
#                     'correct_answer': '',
#                     'time_to_answer': '',
#                     'media_data': [
#                         {
#                             'show_image': '',
#                             'video': {
#                                 'before': '',
#                                 'after': '',
#                             },
#                             'image': {
#                                 'before': '',
#                                 'after': '',
#                                 'player_displayed': '',
#                             },
#                         },
#                     ],
#                 },
#             ],
#         },
#     ]

#     result = {
#         "game": {
#             "game_info": {
#                 **game_info,
#             },
#             'game_settings': {
#                 'tactics': {
#                     **game_settings_tactics,
#                 },
#                 'skip_emails': game.skip_emails,
#             },
#             'rounds': {
#                 game.round_set.values().filter(),
#             },
#         },
#     }

#     return game


def create_question(data):
    media_data = data['media_data']
    question = Question.objects.create(
        question_type=data['type'],
        question_text=data['question'],
        time_to_answer=data['time_to_answer'],
        show_image=media_data['show_image'],
        image_before=media_data['image']['before'],
        image_after=media_data['image']['before'],
        video_before=media_data['video']['before'],
        video_after=media_data['video']['after'],
        correct_answer=data['correct_answer'],
        answers=data['answers']
    )

    # for answer in data['answers']:
    #     AnswerOptions.objects.create(
    #         quest_id=question,
    #         answer=answer,
    #         answer_is_correct=answer==data['correct_answer'],
    #     )

    if data['round_id']:
        question.add(Round.objects.get(id=data['round_id']))

    return model_to_dict(question), True


def get_one_question(data, *args, **kwargs):

    question = Question.objects.get(id=kwargs['pk'])
    #answer_options = question.answeroptions_set.all().values()

    result = {
        "type": question.question_type,
        "question": question.question_text,
        "answers": question.answer,
        "correct_answer": question.correct_answer,
        "time_to_answer": question.time_to_answer,
        "media_data": {
            "show_image": question.show_image,
            "video": {
                "before": question.video_before,
                "after": question.video_after,
            },
            "image": {
                "before": question.image_before,
                "after": question.image_before,
                "player_displayed": question.player_displayed,
            },
        },
    }

    return result


def create_custom_style(document) -> None:
    """Метод создания кастомных стилей для оформления word."""

    from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
    from docx.shared import Pt

    custom_game_name_header = document.styles.add_style('Header game', 1)
    custom_game_name_header.font.bold = True
    custom_game_name_header.font.size = Pt(18)
    custom_game_name_header.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    custom_theme_header = document.styles.add_style('Header theme', 1)
    custom_theme_header.font.size = Pt(16)
    custom_theme_header.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    custom_theme_info = document.styles.add_style('Info theme', 1)
    custom_theme_info.font.size = Pt(14)

    ordered_list = doc.add_paragraph(style='ListNumber')

    return custom_game_name_header, custom_theme_header, custom_theme_info
