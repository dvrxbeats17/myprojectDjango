# Generated by Django 5.0.6 on 2024-08-14 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'get_latest_by': 'pub_date'},
        ),
    ]
