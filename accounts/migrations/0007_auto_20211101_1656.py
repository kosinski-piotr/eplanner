# Generated by Django 3.0.8 on 2021-11-01 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20211101_1656'),
        ('accounts', '0006_auto_20211101_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Class', to='planner.Class'),
        ),
    ]
