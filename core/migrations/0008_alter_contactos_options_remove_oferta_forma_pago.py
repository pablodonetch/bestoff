# Generated by Django 4.1.1 on 2022-12-09 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_contactos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactos',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='forma_pago',
        ),
    ]