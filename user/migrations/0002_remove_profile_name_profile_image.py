# Generated by Django 4.0.7 on 2022-09-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='Profile_Images'),
        ),
    ]
