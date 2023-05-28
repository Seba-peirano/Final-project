from django import forms

class PostFormulario(forms.Form):
    titulo=forms.CharField(required=True, max_length=64)
    subtitulo=forms.CharField(required=True, max_length=64)
    cuerpo=forms.CharField(required=True, max_length=5000)
    #falta fehca
    #falta imagen
    #falta autor automatico
class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(required=True, max_length=64)
    apellido=forms.CharField(required=True, max_length=64)
    email=forms.EmailField(required=True)

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(required=True, max_length=64)
    comision=forms.IntegerField(required=True, max_value=5000)
    curso=forms.CharField(required=True, max_length=64)
    comision=forms.CharField(required=True, max_length=64)

