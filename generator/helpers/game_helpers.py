from typing import (
    Dict,
    Tuple,
    List,
)

from django.forms.models import (
    model_to_dict,
)
from docx.enum.text import (
    WD_PARAGRAPH_ALIGNMENT,
)
from docx.shared import (
    Pt,
)

from generator.models import (
    Game, 
    Question,
    Round,
)


def create_game(data) -> Tuple[Dict, bool]:

    game = Game.objects.create(
        **data.get('game')['game_info'],
        **data.get('game')['game_settings']['tactics'],
        skip_emails=data.get('game')['game_settings']['skip_emails'],
    )

    rounds = data.get('game')['rounds']

    for current_round in rounds:
        questions = current_round.pop('questions')
        _round = Round.objects.create(
            game_id=game,
            round_type=current_round['type'],
            **current_round['settings'],
        )

        for current_question in questions:
            answerZ = current_question['answers']
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
                answers=answerZ,
                correct_answer=current_question['correct_answer']
            )
            question.round_id.add(_round)

    return model_to_dict(game), True


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


def create_custom_style(document) -> None:
    """Метод создания кастомных стилей для оформления word."""

    custom_game_name_header = document.styles.add_style('Header game', 1)
    custom_game_name_header.font.bold = True
    custom_game_name_header.font.size = Pt(18)
    custom_game_name_header.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    custom_theme_header = document.styles.add_style('Header theme', 1)
    custom_theme_header.font.size = Pt(16)
    custom_theme_header.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    custom_theme_info = document.styles.add_style('Info theme', 1)
    custom_theme_info.font.size = Pt(14)

    return custom_game_name_header, custom_theme_header, custom_theme_info


def get_game(id_):
    needed_fields = [
        'id', 
        'question_type',
        'question_text',
        'show_image',
        'image_before',
        'image_after',
        'video_before',
        'video_after',
        'player_displayed',
        'time_to_answer',
        'answers',
        'correct_answer',
        'open_question',
        'close_question',
        'media_question',
        'category__name',
        'round_id__id',
    ]

    game = Game.objects.get(id=id_)
    rounds = game.round_set.all()

    answer = {
        **model_to_dict(game),
        'rounds': [
            {
                **model_to_dict(round_),
                'questions': round_.question_set.all().values(*needed_fields),
            }
            for round_ in rounds
        ]
    }

    return answer


def get_selected_games(ids: List[int]) -> Dict:
    result = {}
    for id_ in ids:
        result[f'game{int(id_)}'] = get_game(int(id_))

    return result
