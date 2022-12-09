from email.mime import image
from unittest import result
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from core.models import *
from bestoff.forms import *
from django.http import HttpResponse, Http404, HttpResponseRedirect

UF=34500 #CAMBIAR UF ACÁ

def home(request):
    propiedades = Propiedad.objects.all()
    images = Image.objects.all()
    rentabilidades=[]
    rentabilidades.append({})
    plusvalia=[]
    plusvalia.append({})
    if request.method == 'POST':
        form_contacto = formulario_contacto(request.POST)
        if form_contacto.is_valid():
            data = form_contacto.cleaned_data
            save = Contactos()
            save.nombre = data['nombre']
            save.email = 'no email'
            save.telefono = data['telefono']
            save.mensaje = data['mensaje']
            save.save()
            form_contacto = formulario_contacto()
    else:
        form_contacto = formulario_contacto()
    for propiedad in propiedades:
        rentabilidades[0][propiedad.id]=float(f'{((propiedad.arriendo_actual*12)/(propiedad.precio*UF)*100):.1f}')
        plusvalia[0][propiedad.id]= float(f'{((1-(propiedad.precio/propiedad.tasacion_comercial))*100):.1f}')
    context={ 
        'propiedades': propiedades,
        'images': images,
        'rentabilidades': rentabilidades,
        'plusvalia': plusvalia,
        'form_contacto': form_contacto,
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