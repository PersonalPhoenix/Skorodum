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
    names_team_members = models.BooleanField(
        verbose_name='Имена членов команд',
        default=False,
    )
    skip_emails = models.BooleanField(
        verbose_name='Email членов команд',
        default=False,
    )
    table_number = models.BooleanField(
        verbose_name='Номер стола',
        default=False,
    )


class File(models.Model):
    """Модель для загружаемых файлов."""

    media_file = models.FileField(
        upload_to='media/',
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )


class Round(models.Model):
    """Модель раунда."""

    class Meta:
        db_table = 'rounds'

    name = models.CharField(
        verbose_name='Имя раунда',
        max_length=300,
    )
    simple_round = models.BooleanField(
        verbose_name='Простой раунд',
        default=False,
    )
    test_round = models.BooleanField(
        verbose_name='Тестовый раунд',
        default=False,
    )
    blitz = models.BooleanField(
        verbose_name='Блиц раунд',
        default=False,
    )
    game_id = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE,
    )
    delete_wrong_answer = models.SmallIntegerField(
        verbose_name='Удалить не верный ответ',
        default=0,
    )
    bet_on = models.SmallIntegerField(
        verbose_name='Ставлю на',
        default=0,
    )
    one_for_all = models.SmallIntegerField(
        verbose_name='Все за одного',
        default=0,
    )
    all_in = models.SmallIntegerField(
        verbose_name='Ва-банк',
        default=0,
    )
    points_per_barrel = models.SmallIntegerField(
        verbose_name='Баллы на бочку',
        default=0,
    )
    answer_time = models.SmallIntegerField(
        verbose_name='Время на ответ',
        default=0,
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
