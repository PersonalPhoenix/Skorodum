# Generated by Django 5.0.2 on 2024-03-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_question_correct_answer_alter_question_image_after_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.CharField(max_length=300),
        ),
    ]