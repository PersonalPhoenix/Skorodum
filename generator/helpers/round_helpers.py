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


def get_one_round(request, *args, **kwargs):
    _round = Round.objects.prefetch_related('question_set').get(id=kwargs['pk'])

    return {
        **model_to_dict(_round),
        'questions': list(
            (i for i in _round.question_set.all().values()),
        ),
    }
