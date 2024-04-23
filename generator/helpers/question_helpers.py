from django.forms.models import (
    model_to_dict,
)

from generator.models import (
    Question,
    Round,
)


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

    if data['round_id']:
        question.add(Round.objects.get(id=data['round_id']))

    return model_to_dict(question), True


def get_one_question(data, *args, **kwargs):

    question = Question.objects.get(id=kwargs['pk'])

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
