"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contol_estudios.views import *

urlpatterns = [
    path("estudiantes/",lista_estudiantes, name="lista_estudiantes"),
    path("cursos/", lista_cursos, name="lista_cursos"),
    path("crear-curso/",formulario_crear_curso, name="crear_curso" ),
    path("crear-estudiante/",formulario_crear_estudiante, name="crear_estudiante" ),
    path("buscar-curso/",buscar_cursos, name="buscar_curso" ),
    path("buscar-estudiante/",buscar_estudiantes, name="buscar_estudiante" ),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path("aboutme/",aboutme, name="aboutme" ),
    path("post-detalle/",PostDetalle, name="postdetalle" ),

    ]