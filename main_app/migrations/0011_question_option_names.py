# Generated by Django 4.1.2 on 2022-10-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_remove_question_option_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_names',
            field=models.CharField(default='foo', max_length=50),
            preserve_default=False,
        ),
    ]
