# Generated by Django 5.0.3 on 2024-03-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0008_file_delete_mediafile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_to_answer',
            field=models.PositiveIntegerField(default=40),
        ),
    ]