# Generated by Django 4.1.5 on 2023-03-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0012_alter_producto_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='descripcion',
            new_name='envio',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='idnumber',
            new_name='pago',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='compra',
            name='mensaje',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='compra',
            name='username',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='mensaje',
            field=models.CharField(default='', max_length=200),
        ),
    ]
