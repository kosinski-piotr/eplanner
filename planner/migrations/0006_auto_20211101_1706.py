# Generated by Django 3.0.8 on 2021-11-01 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20211101_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='is_active',
        ),
    ]
