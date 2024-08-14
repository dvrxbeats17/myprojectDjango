# Generated by Django 5.0.6 on 2024-06-07 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=200)),
                ('number_of_purchases', models.PositiveIntegerField()),
                ('rate', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=200)),
                ('number_of_purchases', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('F', 'Fashion'), ('B', 'Business'), ('S', 'Scinetific')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsPapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=200)),
                ('number_of_purchases', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('newspappers', models.ManyToManyField(to='polygraphy.newspapper')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsPappers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polygraphy.newspapper')),
            ],
        ),
        migrations.CreateModel(
            name='Redactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('books', models.ManyToManyField(to='polygraphy.book')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]