# Generated by Django 4.1.1 on 2023-08-02 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_usersmetadata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersmetadata',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usersmetadata',
            name='slug',
        ),
    ]
