# Generated by Django 4.1.2 on 2022-10-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_question_delete_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='query',
            field=models.BooleanField(default=False),
        ),
    ]