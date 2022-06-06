from django.shortcuts import render
from django.urls import reverse_lazy

from app1.forms import *
from .models import *

from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView


# Create your views here.

@login_required
def inicio(request):

    
    return render(request, 'app1/inicio.html')

# formulario ------------------------------------------------------------------------------------

@login_required
def proyecto(request):

    if request.method == "POST":

        iformulario=ProyectosFormulario(request.POST)

        if iformulario.is_valid():
            informacion=iformulario.cleaned_data
            proyecto=Proyectos(nombre=informacion["nombre"],ingenieroACargo=informacion["ingenieroACargo"], estatus=informacion["estatus"])
            proyecto.save()
            return render(request, 'app1/inicio.html')

    else:
        iformulario=ProyectosFormulario()

    return render(request, 'app1/proyectos.html', {'formulario':iformulario})

# formulario ------------------------------------------------------------------------------------

def tools(request):

    if request.method == "POST":

        iformulario=ToolsFormulario(request.POST)

        if iformulario.is_valid():
            informacion=iformulario.cleaned_data
            tools=inventario_Tools(nombre=informacion["nombre"],cantidad=informacion["cantidad"], ubicacion=informacion["ubicacion"])
            tools.save()
            return render(request, 'app1/inicio.html')

    else:
        iformulario=ToolsFormulario()

    return render(request, 'app1/tools.html', {'formulario':iformulario})

# formulario ------------------------------------------------------------------------------------

def ingenieros(request):

    if request.method == "POST":

        iformulario=IngenieroFormulario(request.POST)

        if iformulario.is_valid():
            informacion=iformulario.cleaned_data
            ingeniero=Ingenieros(nombre=informacion["nombre"],apellido=informacion["apellido"])
            ingeniero.save()
            return render(request, 'app1/inicio.html')

    else:
        iformulario=IngenieroFormulario()

    return render(request, 'app1/ingenieros.html', {'formulario':iformulario})

#Busqueda de ingenieros-----------------------------------------------------------------------------------------

def buscarIngeniero(request):
    return render(request, 'app1/busquedaIngeniero.html')

def buscar(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        ingenieros=Ingenieros.objects.filter(nombre=nombre)
        return render(request, 'app1/resultadoBuscar.html', {'ingenieros': ingenieros, 'nombre': nombre})
    else:
        respuesta="No se ingresaron datos"
        return render(request, 'app1/resultadoBuscar.html', {'respuesta': respuesta})


#-----------------------------------------------login---------------------------------------------------------------

def login_request(request):

    if request.method == "POST":
        formulario=AuthenticationForm(request=request, data=request.POST)

        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')
           
            user=authenticate(username=usuario,password=clave)

            if user is not None:
                login(request, user)
                return render(request, 'app1/inicio.html', {'usuerio': usuario, 'mensaje': 'Bienvenido ingresaste al sistema'})
            else:
                return render(request, 'app1/inicio.html', {'mensaje': 'Datos incorrectos'})

        else:
            return render(request, 'app1/inicio.html', {'mensaje': 'Formulario no valido'})

    else:
        formulario=AuthenticationForm()
        return render(request, 'app1/login.html', {'formulario':formulario})

#-------------------------------------------Registro y creacion de usuario-----------------------------------------------------------

def register(request):
    if request.method=='POST':
        formulario=registro_usuario(request.POST)

        if formulario.is_valid():
            usuario=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'app1/inicio.html', {'mensaje': f'Usuario "{usuario}"creado '})
        else:
            return render(request, 'app1/inicio.html', {'mensaje': 'No se creo el usurio'})
    else: 
        formulario=registro_usuario()
        return render(request, 'app1/registro.html', {'formulario':formulario})
        

def perfil(request):
    usuario=request.user

    avatar=Avatar.objects.filter(user=request.user)
    if(len(avatar)!=0):
        avatar=Avatar.objects.filter(user=request.user)
    
        return render(request, 'app1/perfil.html', {'username':usuario.username, 'url': avatar[0].avatar.url})
    else:
        return render(request, 'app1/perfil.html', {'username':usuario.username})
            
    

@login_required
def editarUsuario(request):
    usuario=request.user

    if request.method=='POST':
       formulario=UserEditForm(request.POST, instance= usuario)

       if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            mensaje="usuario editado"
       
            return render(request, 'app1/perfil.html', {'mensaje' : mensaje})
    else:
        formulario=UserEditForm(instance=usuario)
        return render(request, 'app1/editarUsuario.html', {'formulario': formulario, 'usuario': usuario.username})


@login_required
def borrarUsuario(request):
    usuario=request.user
    usuario.delete()

    mensaje="Perfil eliminado"
    return render(request, 'app1/inicio.html', {'mensaje' : mensaje})


#---------------------------------------blog ---------------------------------

class BlogList(ListView):
    model= Blog
    template_name= 'app1/blog_listar.html'

class BlogDetalle(DetailView):
    model= Blog
    template_name= 'app1/blog_detalle.html'

class BlogCrear(CreateView):
    model= Blog
    success_url= reverse_lazy('blog_listar')
    fields=('titulo','subtitulo','fecha_creacion', 'cuerpo', 'creador', 'imagen')

class BlogEditar(UpdateView):
    model= Blog
    success_url= reverse_lazy('blog_listar')
    fields=('titulo','subtitulo','fecha_creacion', 'cuerpo', 'creador', 'imagen')

class BlogBorrar(DeleteView):
    model= Blog
    success_url= reverse_lazy('blog_listar')
    fields=('titulo','subtitulo','fecha_creacion', 'cuerpo', 'creador', 'imagen')

#-----------------------------------------------------------------------------------------------


def about(request):
    return render(request, 'app1/about.html')


@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():

            listaAvatares=Avatar.objects.filter(user=request.user)
            
            if(len(listaAvatares)!=0):

                avatarViejo=listaAvatares[0]
                avatarViejo.delete()
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'app1/inicio.html', {'usuario':user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'app1/agregarAvatar.html', {'formulario':formulario, 'usuario':user})
