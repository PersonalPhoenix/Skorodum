from django.forms.models import (
    model_to_dict,
)

from generator.models import (
    Round,
    Game,
    Question,
)


def create_round(data):
    game = Game.objects.get(id=data['game_id'])
    _round = Round.objects.create(
        game_id=game,
        round_type=data['type'],
        **data['settings'],
    )

    questions = data.pop('questions')

    for current_question in questions:
        answerZ = current_question('answers').strip('[]')
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

    return model_to_dict(_round), True


def update_round(request, *args, **kwargs):
    selected_round = Round.objects.get(id=kwargs['pk'])

    # Обязательные поля.
    selected_round.name = kwargs['name']
    selected_round.simple_round = kwargs['simple_round']
    selected_round.test_round = kwargs['test_round']
    selected_round.blitz = kwargs['blitz']

    # Необязательные поля.
    selected_round.game_id = kwargs['game_id']
    selected_round.delete_wrong_answer = kwargs['delete_wrong_answer']
    selected_round.bet_on = kwargs['bet_on']
    selected_round.one_for_all = kwargs['one_for_all']
    selected_round.all_in = kwargs['all_in']
    selected_round.points_per_barrel = kwargs['points_per_barrel']
    selected_round.answer_time = kwargs['answer_time']

    selected_round.save()
