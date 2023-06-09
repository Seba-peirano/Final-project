# Generated by Django 4.2.1 on 2023-05-27 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contol_estudios', '0007_curso_creador_post_creador_socio_creador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('fecha_entrega', models.DateTimeField()),
                ('esta_aprobado', models.BooleanField(default=False)),
                ('creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='esta_aprobado',
        ),
        migrations.RemoveField(
            model_name='post',
            name='fecha_entrega',
        ),
        migrations.AddField(
            model_name='post',
            name='comision',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
