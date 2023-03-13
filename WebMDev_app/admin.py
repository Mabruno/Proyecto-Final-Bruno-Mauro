from django.contrib import admin
from .models import Producto, Usuario, Compra, Consulta

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Consulta)
admin.site.register(Compra)
