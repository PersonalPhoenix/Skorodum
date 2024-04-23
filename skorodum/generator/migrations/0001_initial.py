# Generated by Django 5.0.2 on 2024-04-23 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование категории')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(upload_to='media/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя игры')),
                ('theme', models.CharField(max_length=300, verbose_name='Тема игры')),
                ('client', models.CharField(max_length=300, verbose_name='Заказчик')),
                ('date', models.CharField(max_length=300, verbose_name='Дата игры')),
                ('names_team_members', models.BooleanField(default=False, verbose_name='Имена членов команд')),
                ('skip_emails', models.BooleanField(default=False, verbose_name='Email членов команд')),
                ('table_number', models.BooleanField(default=False, verbose_name='Номер стола')),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя раунда')),
                ('simple_round', models.BooleanField(default=False, verbose_name='Простой раунд')),
                ('test_round', models.BooleanField(default=False, verbose_name='Тестовый раунд')),
                ('blitz', models.BooleanField(default=False, verbose_name='Блиц раунд')),
                ('delete_wrong_answer', models.SmallIntegerField(default=0, verbose_name='Удалить не верный ответ')),
                ('bet_on', models.SmallIntegerField(default=0, verbose_name='Ставлю на')),
                ('one_for_all', models.SmallIntegerField(default=0, verbose_name='Все за одного')),
                ('all_in', models.SmallIntegerField(default=0, verbose_name='Ва-банк')),
                ('points_per_barrel', models.SmallIntegerField(default=0, verbose_name='Баллы на бочку')),
                ('answer_time', models.SmallIntegerField(default=0, verbose_name='Время на ответ')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.game')),
            ],
            options={
                'db_table': 'rounds',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(max_length=300)),
                ('question_text', models.CharField(max_length=300)),
                ('show_image', models.BooleanField(default=False)),
                ('image_before', models.CharField(blank=True, max_length=300, null=True)),
                ('image_after', models.CharField(blank=True, max_length=300, null=True)),
                ('video_before', models.CharField(blank=True, max_length=300, null=True)),
                ('video_after', models.CharField(blank=True, max_length=300, null=True)),
                ('player_displayed', models.BooleanField(default=False)),
                ('time_to_answer', models.PositiveIntegerField(default=40)),
                ('answers', models.CharField(blank=True, max_length=300, null=True)),
                ('correct_answer', models.CharField(blank=True, max_length=300)),
                ('category', models.ManyToManyField(to='generator.category')),
                ('round_id', models.ManyToManyField(blank=True, to='generator.round')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
    ]
