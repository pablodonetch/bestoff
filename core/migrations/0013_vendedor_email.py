# Generated by Django 4.1.1 on 2022-12-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_oferta_aceptada'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='email',
            field=models.CharField(default='ejemplo@ejemplo.cl', max_length=50),
            preserve_default=False,
        ),
    ]
