# Generated by Django 5.0.6 on 2024-08-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaspi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='name',
            field=models.TextField(default='good', max_length=250),
        ),
    ]
