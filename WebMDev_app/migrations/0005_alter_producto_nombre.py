# Generated by Django 4.1.5 on 2023-03-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0004_usuario_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default='', max_length=40),
        ),
    ]
