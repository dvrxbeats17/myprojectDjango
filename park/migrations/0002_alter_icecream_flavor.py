# Generated by Django 5.0.6 on 2024-08-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='flavor',
            field=models.CharField(choices=[('C', 'Chocolate'), ('V', 'Vanilla'), ('M', 'Mint')], max_length=200),
        ),
    ]
