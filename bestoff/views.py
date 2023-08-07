from email.mime import image
from unittest import result
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from core.models import *
from bestoff.forms import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from collections import defaultdict

UF=35200 #CAMBIAR UF ACÁ

def home(request):
    usersMetadata=''
    if request.user.is_authenticated:
        usersMetadata = UsersMetadata.objects.filter(user_id=request.user.id).get()
    propiedades= Propiedad.objects.all()
    propiedades_diccionario=defaultdict(dict)
    for i in range(0,propiedades.count()):
        propiedades_diccionario[propiedades[i].id]['id']=propiedades[i].id
        propiedades_diccionario[propiedades[i].id]['comuna']=propiedades[i].comuna.comuna
        propiedades_diccionario[propiedades[i].id]['precio']=float(f'{propiedades[i].precio}')
        propiedades_diccionario[propiedades[i].id]['rentabilidad']=(float(f'{((propiedades[i].arriendo_actual*12)/(propiedades[i].precio*UF)*100):.1f}'))
        propiedades_diccionario[propiedades[i].id]['plusvalia']=(float(f'{((propiedades[i].tasacion_comercial*100/propiedades[i].precio)-100):.1f}'))
        propiedades_diccionario[propiedades[i].id]['propiedad_bancaria']=propiedades[i].propiedad_bancaria
    propiedades_diccionario = dict(propiedades_diccionario)
    form_buscar=formulario_buscar()
    images = Image.objects.all()
    context={
        'portada':'propiedades',
        'propiedades': propiedades, 
        'propiedades_diccionario':propiedades_diccionario,
        'images': images, 
        'formulario_buscar': form_buscar,
        'usermetadata':usersMetadata,
    }
    return render(request, 'propiedades/buscador.html', context)


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