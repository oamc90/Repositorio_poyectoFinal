from django.urls import path
from .views import *

urlpatterns = [
    path('mensajes/', mensajeList, name='mensaje_listar'),
    path('mensaje/<id>', mensajeDetalle , name='mensaje_detalle'),
    path('mensaje/nuevo/', mensajeCrear , name='mensaje_crear'),
    path('mensajes/editar/<id>', mensajeEditar , name='mensaje_editar'),
    path('mensajes/borrar/<id>', mensajeBorrar , name='mensaje_borrar'),  
    path('listaUsuarios', usuariosList , name='lista_usuario'),
    
  
    
]