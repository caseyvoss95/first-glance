# Generated by Django 4.1.2 on 2022-10-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_question_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='query',
            field=models.CharField(max_length=200),
        ),
    ]