# Generated by Django 5.0.6 on 2024-08-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.TextField(max_length=200)),
                ('LastName', models.TextField(max_length=200)),
                ('cv', models.FileField(upload_to='file')),
                ('photo', models.ImageField(upload_to='file')),
                ('id_photo', models.ImageField(upload_to='file')),
            ],
        ),
    ]