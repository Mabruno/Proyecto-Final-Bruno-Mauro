# Generated by Django 4.1.5 on 2023-03-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0011_remove_user_mensaje_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]