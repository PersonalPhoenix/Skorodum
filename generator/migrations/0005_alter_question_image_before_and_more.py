# Generated by Django 5.0.2 on 2024-07-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_alter_question_image_after'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image_before',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='video_after',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='video_before',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
