# Generated by Django 3.2.12 on 2022-11-22 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_scene_devices_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene_devices',
            name='date',
        ),
    ]
