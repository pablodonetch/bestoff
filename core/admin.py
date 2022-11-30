from django.contrib import admin
from pathlib import Path
from django.utils.html import format_html
from .models import *
from django.conf import settings
import os


admin.site.site_header = 'Administración de Propiedades'
admin.site.site_title = 'Donetch & Cía. Administración'
admin.site.index_title = 'Administración de Propiedades'

class MonedasAdmin(admin.ModelAdmin):
    list_display = ('id','moneda',)

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'direccion', 'tipo_propiedad', 'tipo_operacion', 'comuna', 'precio', 'destacado')
    list_filter = ('tipo_propiedad', 'tipo_operacion', 'comuna')
    search_fields = ('direcicon', 'descripcion')
    list_per_page = 10

def mostrar_imagen(obj):
    return format_html(f""" <a href="/media/{obj.image}" target="_blank">
		<img src="/media/{obj.image}" width="100" height="70" />
		</a> """)
mostrar_imagen.short_description = 'Imagen' 

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_propiedades', 'image', mostrar_imagen)
    list_filter = ('id_propiedades',)
    search_fields = ('id_propiedades',)
    list_per_page = 10

#Ver Foto Miniatura
#def foto_miniatura(self):
#    print(settings.MEDIA_URL)
#    return format_html('<img src="{}/{}" target="blank" width="100" height="100" />'.format(settings.MEDIA_URL,ojb.image.url))



admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Documentos_Legales)
admin.site.register(Vendedor)
admin.site.register(comuna)

#información básica para empezar a ingresar propiedades
#admin.site.register(tipo_operacion)
#admin.site.register(tipo_propiedad)
admin.site.register(moneda, MonedasAdmin)
admin.site.register(Oferta)
admin.site.register(Comprador)
admin.site.register(Estado_Oferta)
#admin.site.register(Corredor)
#admin.site.register(metodo_pago) #no se usa
#admin.site.register(Estado_Ocupacion)