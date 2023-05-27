from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from contol_estudios.models import *
from contol_estudios.forms import *




def lista_estudiantes(request):
    contexto={
        "estudiantes": Socio.objects.all()
    }
    http_responde=render(
    request= request,
    template_name='contol_estudios/lista_estudiantes.html',
    context= contexto,
    )
    return http_responde


def lista_cursos(request):
    contexto={
        "posts": Post.objects.all()
    }
    http_responde=render(
    request= request,
    template_name='contol_estudios/lista_cursos.html',
    context= contexto,
    )
    return http_responde

@login_required
def formulario_crear_curso(request):
    if request.method == "POST":
        formulario=PostFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre= data["nombre"]
            comision=data["comision"]
            creador=request.user
            post=Post( nombre=nombre, comision=comision, creador=creador)
            post.save()
            #redirecciono al usuario a la lista de cursos
            url_exitosa=reverse('lista_cursos')
            return redirect(url_exitosa)

    else: #GET
        formulario=PostFormulario()
        http_response=render(
            request= request,
            template_name='contol_estudios/formulario_crear_curso.html',
            context= {'formulario': formulario},
            )
        return http_response
    

def buscar_cursos(request):
    if request.method == "POST":
        data=request.POST
        busqueda= data["busqueda"]
        posts=Post.objects.filter(nombre__icontains=busqueda)
        contexto={
            "posts": posts,
        }
        http_response=render(
            request= request,
            template_name='contol_estudios/lista_cursos.html',
            context= contexto,
            )
        return http_response

@login_required
def formulario_crear_estudiante(request):
    if request.method == "POST":
        formulario=EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre= data["nombre"]
            apellido=data["apellido"]
            email=data["email"]
            estudiante=Estudiante( nombre=nombre,apellido=apellido,email=email)
            estudiante.save()
            #redirecciono al usuario a la lista de estudiantes
            url_exitosa=reverse('lista_estudiantes')
            return redirect(url_exitosa)

    else: #GET
        formulario=EstudianteFormulario()
        http_response=render(
            request= request,
            template_name='contol_estudios/formulario_crear_estudiante.html',
            context= {'formulario': formulario},
            )
        return http_response


def buscar_estudiantes(request):
    if request.method == "POST":
        data=request.POST
        busqueda= data["busqueda"]
        estudiante=Estudiante.objects.filter(apellido__contains=busqueda)
        contexto={
            "Estudiante": estudiante,
        }
        http_response=render(
            request= request,
            template_name='contol_estudios/lista_estudiantes.html',
            context= contexto,
            )
        return http_response

def eliminar_curso(request, id):
   post = Post.objects.get(id=id)
   if request.method == "POST":
       post.delete()
       url_exitosa = reverse('lista_cursos')
       return redirect(url_exitosa)

def editar_curso(request, id):
   post = Post.objects.get(id=id)
   if request.method == "POST":
       formulario = PostFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           post.nombre = data['nombre']
           post.comision = data['comision']
           post.save()
           url_exitosa = reverse('lista_cursos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': post.nombre,
           'comision': post.comision,
       }
       formulario = PostFormulario(initial=inicial)
   return render(
       request=request,
       template_name='contol_estudios/formulario_crear_curso.html',
       context={'formulario': formulario},
   )