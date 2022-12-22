from django.contrib.sitemaps import Sitemap # Importamos la clase Sitemap
from core.models import *

class PropiedadesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Propiedad.objects.all()

    def location(self, obj):
        return f'propiedades/detalles/0/{obj.id}/{str(obj.comuna).replace(" ","-")}-{str(obj.direccion).replace(" ","-")}'