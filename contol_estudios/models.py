from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    nombre=models.CharField(max_length=30) #titulo
    comision=models.CharField(max_length=30) #subtitulo
    cuerpo=models.CharField(max_length=20000) 
    # autor=models.CharField(max_length=30) ver como sacarlo del creador
    fecha=models.DateTimeField(null=True)
    imagen = models.ImageField(upload_to='post_images')  # Campo para la imagen
    creador=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self) :
        return f"{self.nombre}| {self.comision}"
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    
class Socio(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()
    creador=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Visitante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()

class Entregable(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField()
    esta_aprobado=models.BooleanField(default=False)
    creador=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    