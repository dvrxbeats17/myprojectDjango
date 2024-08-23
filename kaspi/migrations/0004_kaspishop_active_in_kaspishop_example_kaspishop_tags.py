# Generated by Django 5.0.6 on 2024-08-23 15:46

import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaspi', '0003_rename_shop_kaspishop_revkaspishop_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaspishop',
            name='active_in',
            field=django.contrib.postgres.fields.ranges.DateRangeField(default='2024-12-12', verbose_name='Активен между'),
        ),
        migrations.AddField(
            model_name='kaspishop',
            name='example',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(default='2024-12-01', verbose_name='Example'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kaspishop',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), default=[''], size=None, verbose_name='Tags'),
            preserve_default=False,
        ),
    ]
