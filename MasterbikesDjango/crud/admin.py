from django.contrib import admin
from .models import *

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')
    list_display = ('descripcion','marca','precio','stock')
    ordering = ('creado',)

class MarcaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','creado','actualizado')
    list_display = ('marca',)
    ordering = ('marca',)

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Marca,MarcaAdmin)