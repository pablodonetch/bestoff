# Generated by Django 4.1.1 on 2022-12-07 22:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_ofertas_oferta_alter_oferta_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
