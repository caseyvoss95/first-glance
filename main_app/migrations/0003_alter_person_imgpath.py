# Generated by Django 4.1.2 on 2022-10-23 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='imgPath',
            field=models.TextField(max_length=500),
        ),
    ]
