# Generated by Django 4.2.1 on 2023-05-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contol_estudios', '0009_post_cuerpo_post_fecha_post_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]