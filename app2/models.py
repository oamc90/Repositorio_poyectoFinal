from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Mensaje(models.Model):
    usuarios=User.objects.all()
    numero=1
    lista_usuario=[]
    for usuarios in usuarios: 
        numero=numero+1
        lista=(numero,usuarios)
        lista_usuario.append(lista)
    
    emisor=models.CharField(max_length=50)
    receptor=models.CharField(max_length=50, choices=lista_usuario)
    contenido=RichTextField(blank=True, null=True)
    fecha_envio=models.TextField(default=str(datetime.now()))
    



