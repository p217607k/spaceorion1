# Generated by Django 3.2.12 on 2022-11-22 05:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_scene_devices_time_scene_devices_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scene_devices',
            old_name='scene_device_type',
            new_name='scene_device_type1',
        ),
        migrations.RenameField(
            model_name='scene_devices',
            old_name='status',
            new_name='status1',
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type10',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type2',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type3',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type4',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type5',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type6',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type7',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type8',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='scene_device_type9',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status10',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status2',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status3',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status4',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status5',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status6',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status7',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status8',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene_devices',
            name='status9',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
    ]
