from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),
    path('ingenieros/',ingenieros, name='ingeniero'),
    path('proyectos/',proyecto, name='proyecto'),
    path('tools/',tools, name='tools'),
   # path('ingenierosFormulario/',ingenierosFormulario, name='ingenierosFormulario'),
    path('busquedaIngeniero/',buscarIngeniero, name='busquedaIngeniero'),
    path('buscar/',buscar, name='buscar'),

    path('about/', about , name='about'),
    path('profile/', perfil , name='perfil'),
    path('eliminarPerfil/', borrarUsuario , name='eliminarPerfil'),
    path('editarUsuario/', editarUsuario , name='editarUsuario'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),


    path('login/', login_request, name='login'),
    path('registro/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name="app1/logout.html") , name='logout'),


    path('pages', BlogList.as_view() , name='blog_listar'),
    path('blog/<pk>/', BlogDetalle.as_view() , name='blog_detalle'),
    path('blogs/nuevo/', BlogCrear.as_view() , name='blog_crear'),
    path('blog/editar/<pk>/', BlogEditar.as_view() , name='blog_editar'),
    path('blog/borrar/<pk>/', BlogBorrar.as_view() , name='blog_borrar'),  
  
    
]

