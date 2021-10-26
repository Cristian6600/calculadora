from django.contrib import admin

from . models import Cliente, Factura, Categoria, Ticket, Eventos, Ventas 

@admin.register(Ventas)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('precio_iva', 'precio_sin_iva', 'Cantidad_ticket', 'categoria', 'ticket', 'fecha', 'estado')

    admin.site.register(Cliente)
    admin.site.register(Factura)
    admin.site.register(Categoria)
    admin.site.register(Ticket)
    
    admin.site.register(Eventos)

