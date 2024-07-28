from django.forms.models import (
    model_to_dict,
)

from generator.models import (
    Question,
)


def create_question(data):
    media_data = data.get('media_data')

    if media_data:
        question = Question.objects.create(
            question_type=data['type'],
            question_text=data['question'],
            time_to_answer=data.get('time_to_answer', 0),
            show_image=media_data.get('show_image', False),
            image_before=media_data.get('image', {}).get('before'),
            image_after=media_data.get('image', {}).get('after'),
            video_before=media_data.get('video', {}).get('before'),
            video_after=media_data.get('video', {}).get('after'),
            correct_answer=data['correct_answer'],
            answers=data.get('answers', '')
        )
    else:
        question = Question.objects.create(
            question_type=data['type'],
            question_text=data['question'],
            correct_answer=data['correct_answer'],
        )

    if round_id := data.get('round_id'):
        question.rounds = round_id

    return model_to_dict(question), True


def get_one_question(data, *args, **kwargs):

    question = Question.objects.get(id=kwargs['pk'])

    result = {
        "type": question.question_type,
        "question": question.question_text,
        "answers": question.answers,
        "correct_answer": question.correct_answer,
        "time_to_answer": question.time_to_answer,
        "media_data": {
            "show_image": question.show_image,
            "video": {
                "before": question.video_before or '',
                "after": question.video_after or '',
            },
            "image": {
                "before": question.image_before or '',
                "after": question.image_before or '',
                "player_displayed": question.player_displayed,
            },
        },
    }

    return result
