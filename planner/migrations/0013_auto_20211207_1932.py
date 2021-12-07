# Generated by Django 3.0.8 on 2021-12-07 18:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0012_auto_20211116_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='Date_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 7, 19, 32, 52, 875298), verbose_name='Date start'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='Date_stop',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 7, 19, 32, 52, 876296), verbose_name='Date stop'),
        ),
        migrations.AlterField(
            model_name='userinclass',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classes', to='planner.Class'),
        ),
        migrations.AlterField(
            model_name='userinclass',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
