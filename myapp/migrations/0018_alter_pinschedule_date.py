# Generated by Django 3.2.12 on 2022-11-22 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_pinschedule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinschedule',
            name='date',
            field=models.DateField(default=datetime.date(2022, 11, 22), null=True),
        ),
    ]
