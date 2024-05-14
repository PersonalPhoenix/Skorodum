from django.db import models


class Game(models.Model):
    """Модель игры."""

    class Meta:
        db_table = 'games'

    name = models.CharField(
        verbose_name='Имя игры',
        max_length=300,
    )
    theme = models.CharField(
        verbose_name='Тема игры',
        max_length=300,
    )
    client = models.CharField(
        verbose_name='Заказчик',
        max_length=300,
    )
    date = models.CharField(
        verbose_name='Дата игры',
        max_length=300,
    )
    remove_answer = models.PositiveIntegerField(
        default=0,
    )
    one_for_all = models.PositiveIntegerField(
        default=0,
    )
    question_bet = models.PositiveIntegerField(
        default=0,
    )
    all_in = models.PositiveIntegerField(
        default=0,
    )
    team_bet = models.PositiveIntegerField(
        default=0,
    )
    skip_emails = models.BooleanField(
        default=False,
    )


class File(models.Model):
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Round(models.Model):
    """Модель раунда."""

    class Meta:
        db_table = 'rounds'

    game_id = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE,
    )
    round_type = models.CharField(
        max_length=300,
    )
    is_test = models.BooleanField(
        default=False,
    )
    name = models.CharField(
        max_length=300,
    )
    display_name = models.BooleanField(
        default=False,
    )
    time_to_answer = models.PositiveIntegerField(
        default=0,
    )
    use_special_tactics = models.BooleanField(
        default=False,
    )
    blitz_score = models.CharField(
        max_length=300,
        default='0',
    )


class Category(models.Model):
    """Модель категории."""

    class Meta:
        db_table = 'categories'

    name = models.CharField(
        verbose_name='наименование категории',
        max_length=100,
    )


class Question(models.Model):
    """Модель вопроса"""

    class Meta:
        db_table = 'questions'

    round_id = models.ManyToManyField(
        Round,
        blank=True,
    )
    question_type = models.CharField(
        max_length=300,
    )
    category = models.ManyToManyField(
        Category,
    )
    question_text = models.CharField(
        max_length=300,
    )
    show_image = models.BooleanField(
        default=False,
    )
    image_before = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    image_after = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    video_before = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    video_after = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    player_displayed = models.BooleanField(
        default=False,
    )
    time_to_answer = models.PositiveIntegerField(
        default=40
    )
    answers = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )
    correct_answer= models.CharField(
        max_length=300,
        blank=True
    )
    open_question = models.BooleanField(
        default=False,
    )
    close_question = models.BooleanField(
        default=False,
    )
    media_question = models.BooleanField(
        default=False,
    )
