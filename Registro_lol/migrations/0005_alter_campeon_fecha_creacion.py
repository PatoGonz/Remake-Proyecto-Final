# Generated by Django 4.1.7 on 2023-05-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_lol', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeon',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
