# Generated by Django 3.0.8 on 2021-11-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20211101_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Class name'),
        ),
    ]
