# Generated by Django 3.0.8 on 2021-11-09 17:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0010_auto_20211109_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='Date_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 9, 18, 26, 4, 233981), verbose_name='Date start'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='Date_stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 9, 18, 26, 4, 234975), verbose_name='Date stop'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='Teacher',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_teacher': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]