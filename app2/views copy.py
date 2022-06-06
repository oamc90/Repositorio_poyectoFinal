from django.shortcuts import render

from app2.models import Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

# Create your views here.



class MensajeList(ListView):
    model= Mensaje
    template_name= 'app2/mensaje_listar.html'

class MensajeDetalle(DetailView):
    model= Mensaje
    template_name= 'app2/mensaje_detalle.html'

class MensajeCrear(CreateView):
    model= Mensaje
    success_url= reverse_lazy('mensaje_listar')
    fields=( 'emisor','receptor','fecha_envio', 'contenido')

class MensajeEditar(UpdateView):
    model= Mensaje
    success_url= reverse_lazy('mensaje_listar')
    fields=('emisor','receptor','fecha_envio', 'contenido')

