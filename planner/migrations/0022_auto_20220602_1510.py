# Generated by Django 3.0.8 on 2022-06-02 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0021_auto_20211223_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='Date_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 2, 15, 10, 5, 212200), verbose_name='Date start'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='Date_stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 2, 15, 10, 5, 212200), verbose_name='Date stop'),
        ),
    ]
