# Generated by Django 4.2.1 on 2023-05-25 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contol_estudios', '0003_remove_profesor_bio_remove_profesor_dni_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Socio',
        ),
    ]
