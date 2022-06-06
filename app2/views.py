from collections import UserList
from django.shortcuts import render

from app2.models import Mensaje
from app2.forms import mensajeFormulario
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView 
from django.contrib.auth.models import User

# Create your views here.

@login_required
def mensajeCrear(request):
    usuario=request.user
    receptor=Mensaje.receptor

    if request.method == "POST":

        formulario=mensajeFormulario(request.POST)

        if formulario.is_valid():
            informacion=formulario.cleaned_data
            mensaje=Mensaje(emisor=informacion["emisor"],receptor=informacion["receptor"], contenido=informacion['contenido'])
            mensaje.save() 

            
            return render(request, 'app2/mensaje_listar.html')

    else:
        formulario=mensajeFormulario(initial={'emisor': usuario.username, 'receptor': receptor})
        return render(request, 'app2/mensaje_form.html', {'formulario':formulario})
    


def mensajeList(request):
    mensajes=Mensaje.objects.all()
    contexto={'mensajes': mensajes}
    
    return render(request, 'app2/mensaje_listar.html', contexto)

def mensajeDetalle(request, id):
    codigo=Mensaje.objects.get(id=id)
    contexto={'codigo': codigo}
    
    return render(request, 'app2/mensaje_detalle.html', contexto)


@login_required
def mensajeEditar(request, id):
    mensajes=Mensaje.objects.get(id=id)
    if request.method == 'POST':
        formulario=mensajeFormulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            mensajes.contenido=informacion['contenido']
            mensajes.save()
            

            mensajes=Mensaje.objects.all()
            contexto={'mensajes': mensajes}
        
            return render(request, 'app2/mensaje_listar.html', contexto)
    else:
        formulario=mensajeFormulario(initial={'emisor': mensajes.emisor, 'receptor': mensajes.receptor, 'contenido': mensajes.contenido, })
    return render(request, 'app2/mensaje_editar.html', {'formulario':formulario, 'id':id})



@login_required
def mensajeBorrar(request,id):
    mensajes=Mensaje.objects.get(id=id)
    mensajes.delete()

    mensajes=Mensaje.objects.all()
    contexto={'mensajes': mensajes}
    
    return render(request, 'app2/mensaje_listar.html', contexto)


    
def usuariosList(request):
    usuario=User.objects.all()
    return render(request, 'app2/lista_usuario.html', {'usuario': usuario})

