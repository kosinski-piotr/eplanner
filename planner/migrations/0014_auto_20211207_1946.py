# Generated by Django 3.0.8 on 2021-12-07 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0013_auto_20211207_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='Date_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 7, 19, 46, 45, 152582), verbose_name='Date start'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='Date_stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 7, 19, 46, 45, 152582), verbose_name='Date stop'),
        ),
    ]
