from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .views import *
from .sitemaps import *

sitemaps = {
    'propiedades': PropiedadesSitemap, # El key de este diccionario puede ser cualquier nombre
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('propiedades/', include('propiedades.urls'), name="propiedades_individuales"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('vender/', vender, name='vender'),
    path('quehacemos/', quehacemos, name='quehacemos'),
    path('acceso/', include('acceso.urls'), name='acceso_urls'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)