from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Ingenieros(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cargo=models.CharField(max_length=50)
    proyecto=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre +" "+ self.apellido

class Proyectos(models.Model):
    nombre=models.CharField(max_length=50)
    ingenieroACargo=models.CharField(max_length=50)
    estatus=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre +", Estado:" + self.estatus


class inventario_Tools(models.Model):
    nombre=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    ubicacion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Blog(models.Model):
    creador=models.CharField(max_length=50,null=True)
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=50)
    fecha_creacion=models.TextField(default=str(datetime.now()))
    cuerpo=RichTextField(blank=True, null=True)
    imagen= models.ImageField(upload_to='avatar', blank=True, null=True)
    
    


    def __str__(self):
        return self.titulo



class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)