# Generated by Django 5.1.1 on 2024-09-20 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_login', '0004_alter_gamers_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gamers',
            new_name='User',
        ),
    ]
