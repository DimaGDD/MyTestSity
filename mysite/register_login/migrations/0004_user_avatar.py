# Generated by Django 5.1.1 on 2024-09-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_login', '0003_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
