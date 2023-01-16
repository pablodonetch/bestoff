from email.mime import image
from unittest import result
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from core.models import *
from bestoff.forms import *
from django.http import HttpResponse, Http404, HttpResponseRedirect

UF=35200 #CAMBIAR UF ACÁ

def home(request):
    propiedades = Propiedad.objects.all()
    images = Image.objects.all()
    rentabilidades=[]
    rentabilidades.append({})
    plusvalia=[]
    plusvalia.append({})
    formulario_vender='0'
    diccionario_imagenes=[]
    diccionario_imagenes.append({})
    form_buscar=formulario_buscar()
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
            formulario_vender='1'
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
        'formulario_vender':formulario_vender,
        'formulario_buscar':form_buscar,
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


def vender(request):
    form_vender = formulario_vender()
    contacto_enviado='0'
    if request.method == 'POST':
        data=request.POST
        action = data.get("enviar")
        if action=="vender":
            form_vender=formulario_vender(request.POST)
            if form_vender.is_valid():
                data=form_vender.cleaned_data
                save_contacto=Contactos()
                save_contacto.nombre=data['nombre']
                save_contacto.telefono_contacto=data['telefono']
                save_contacto.email=data['email']
                direccion=data['direccion']
                comuna=data['comuna']
                caracteristicas=data['caracteristicas']
                save_contacto.mensaje=f'Quiero vender: {direccion}, {comuna}, {caracteristicas}'
                save_contacto.save()
                contacto_enviado='1'
            else:
                contacto_enviado='2'
    context={
        'form_vender':form_vender,
        'contacto_enviado':contacto_enviado,
    }
    return render (request, 'pages/vender.html', context)

def quehacemos(request):
    context={

    }
    return render (request, 'pages/que_hacemos.html', context)