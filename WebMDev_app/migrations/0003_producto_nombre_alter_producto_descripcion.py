# Generated by Django 4.1.5 on 2023-03-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0002_consulta_producto_valoracion_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default='none', max_length=40),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
