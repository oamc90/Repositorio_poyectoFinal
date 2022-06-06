from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class IngenieroFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    cargo=forms.CharField(max_length=50)
    proyecto=forms.CharField(max_length=50)

class ProyectosFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    ingenieroACargo=forms.CharField(max_length=50)
    estatus=forms.CharField(max_length=50)


class ToolsFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()
    ubicacion=forms.CharField(max_length=50)

class registro_usuario(UserCreationForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password1', 'password2')
        help_texts={k: " " for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar email")
    password1=forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    #fisrt_name=forms.CharField(label="Modificar nombre", widget=forms.PasswordInput)
    #last_name=forms.CharField(label="Modificar apellido", widget=forms.PasswordInput)
    #avatar=forms.ImageField(label="Avatar")

    class Meta:
        model=User
        fields=('email','password1', 'password2')
        help_texts={k: " " for k in fields}


class AvatarForm(forms.Form):
    avatar= forms.ImageField(label="Avatar")