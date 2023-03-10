# Generated by Django 3.0.8 on 2021-10-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Company name')),
                ('time_interval', models.IntegerField(choices=[[15, 15], [30, 30], [60, 60]], default=15, verbose_name='Time Interval')),
            ],
        ),
    ]
