# Generated by Django 4.1.1 on 2023-08-03 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_propiedad_fecha_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='fecha_termino',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
