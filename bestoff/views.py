from email.mime import image
from unittest import result
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from core.models import *


class HomeView(View):
    def get(self, request, *args, **kwargs):
        propiedades = Propiedad.objects.all()
        images = Image.objects.all()
        UF=34500 #CAMBIAR UF ACÁ
        rentabilidades=[]
        rentabilidades.append({})
        for propiedad in propiedades:
            rentabilidad_real= float(f'{((propiedad.arriendo_actual*12)/(propiedad.precio*UF)*100):.1f}')
            rentabilidades[0][propiedad.id]=rentabilidad_real
        print(rentabilidades)
        context={ 
            'propiedades': propiedades,
            'images': images,
            'rentabilidades': rentabilidades,
        }
        return render(request, 'pages/index.html', context)

#Propiedades se define "2 veces" para que se pueda usar como subdirectorio base
class propiedades(View):
    def get(self, request, *args, **kwargs):
        propiedades = Propiedad.objects.all()
        images = Image.objects.all()
        context={ 
            'propiedades': propiedades,
            'images': images,
        }
        return render(request, 'propiedades/index.html', context)


def list_Propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'pages/index.html', {'propiedades': propiedades})