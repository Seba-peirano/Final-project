# Generated by Django 4.2.1 on 2023-05-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contol_estudios', '0011_remove_post_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
    ]