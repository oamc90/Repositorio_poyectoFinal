from django.contrib import admin
from .models import *

from app1.views import *

# Register your models here.

admin.site.register(Ingenieros)
admin.site.register(Proyectos)
admin.site.register(inventario_Tools)
admin.site.register(Blog)
admin.site.register(Avatar)