# Generated by Django 4.0.4 on 2022-08-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_profile_token_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sender_id',
            field=models.URLField(max_length=700),
        ),
    ]
