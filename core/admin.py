from django.contrib import admin
from pathlib import Path
from django.utils.html import format_html
from .models import *
from django.conf import settings
import os
import boto3


admin.site.site_header = 'Administración de Propiedades'
admin.site.site_title = 'Bestoff. Administración'
admin.site.index_title = 'Administración de Propiedades'

class MonedasAdmin(admin.ModelAdmin):
    list_display = ('id','moneda',)

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'direccion', 'tipo_propiedad', 'tipo_operacion', 'comuna', 'precio', 'destacado')
    list_filter = ('tipo_propiedad', 'tipo_operacion', 'comuna')
    search_fields = ('direcicon', 'descripcion')
    list_per_page = 10

def mostrar_imagen(obj):
    return format_html(f"""<a href="https://bestoff-cl.s3.amazonaws.com/{obj.image}" target="_blank">
		<img src="https://bestoff-cl.s3.amazonaws.com/{obj.image}" width="100" height="70" />
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


class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        # Si el campo es una imagen
        if db_field.name == "image":
            # Crea un cliente de S3
            s3 = boto3.client("s3")

            # Recupera la imagen del almacenamiento de S3
            response = s3.get_object(Bucket="bestoff-cl", Key=db_field.value)

            # Accede al contenido de la imagen como una secuencia de bytes
            image_content = response["Body"].read()

            # Crea una URL a partir de la secuencia de bytes
            image_url = "data:image/jpg;base64," + image_content.encode("base64")
            print(image_url)
            # Muestra la imagen en el formulario del panel de administración
            kwargs["widget"] = admin.widgets.AdminFileWidget(attrs={"data-src": image_url})

        return super(MyModelAdmin, self).formfield_for_dbfield(db_field, **kwargs)

# Registra el modelo y su clase personalizada de ModelAdmin
#admin.site.register(Image, MyModelAdmin)




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
admin.site.register(Contactos)
#admin.site.register(UserAdmin)
admin.site.register(UsersMetadata)
#admin.site.register(Corredor)
#admin.site.register(metodo_pago) #no se usa
#admin.site.register(Estado_Ocupacion)