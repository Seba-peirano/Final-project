# Generated by Django 4.2.1 on 2023-05-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contol_estudios', '0008_entregable_remove_post_esta_aprobado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cuerpo',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='comision',
            field=models.CharField(max_length=30),
        ),
    ]