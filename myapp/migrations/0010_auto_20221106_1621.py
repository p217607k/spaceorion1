# Generated by Django 3.2.12 on 2022-11-06 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_pinschedule_timing1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pinschedule',
            old_name='date1',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='pinschedule',
            old_name='timing1',
            new_name='timing',
        ),
    ]