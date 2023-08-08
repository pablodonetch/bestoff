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
import json

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

def cuentaregresiva(request, propiedad_id):
    propiedad = Propiedad.objects.filter(id=propiedad_id).get()
    propiedad_diccionario_socket={}
    #calulamos el tiempo restante
    ahora = datetime.now()
    # Convertir a objetos naive
    ahora_naive = ahora.replace(tzinfo=None)
    termino_naive = propiedad.fecha_termino.replace(tzinfo=None)
    tiempo_restante = termino_naive - ahora_naive
    dias=tiempo_restante.days
    horas,segundos=divmod(tiempo_restante.seconds, 3600)
    minutos,segundos=divmod(segundos, 60)
    # Ordena los ceros
    str_dias=str(dias)
    if dias<10:
        str_dias='0'+str(dias)
    str_horas=str(horas)
    if horas<10:
        str_horas='0'+str(horas)
    str_minutos=str(minutos)
    if minutos<10:
        str_minutos='0'+str(minutos)
    str_segundos=str(segundos)
    if segundos<10:
        str_segundos ='0'+str(segundos)

    arreglo_html='''<div class="grid grid-cols-5">
            <div class="col grid grid-cols-4">
                <div class="col-span-3 grid grid-row-2">
                    <div class="row">
                        '''+str_dias + '''
                    </div>
                    <div class="row">
                        <p class="text-xs">días</p>
                    </div>
                </div>
                <div class="col">
                    <p class="text-sm">:</p>
                </div>
            </div>
            <div class="col grid grid-cols-4">
                <div class="col-span-3 grid grid-row-2">
                    <div class="row">
                        '''+str_horas + '''
                    </div>
                    <div class="row">
                        <p class="text-xs">hrs</p>
                    </div>
                </div>
                <div class="col">
                    <p class="text-sm">:</p>
                </div>
            </div>
            <div class="col grid grid-cols-4">
                <div class="col-span-3 grid grid-row-2">
                    <div class="row">
                        '''+str_minutos + '''
                    </div>
                    <div class="row">
                        <p class="text-xs">min</p>
                    </div>
                </div>
                <div class="col">
                    <p class="text-sm">:</p>
                </div>
            </div>
            <div class="col grid-row-2">
                <div class="row">
                '''+str_segundos + '''
                </div>
                <div class="row">
                <p class="text-xs">seg</p>
                </div>
            </div>

            </div>
    '''
    cuenta_regresiva = str_dias + ':' + str_horas+':' +str_minutos +':'+str_segundos
    print('id_propiedad: dias ' + str(dias) + ' ;horas ' + str(horas)+' segundos: '+str(segundos))
    propiedad_diccionario_socket={'dias':str_dias,'horas':str_horas,'minutos':str_minutos,'segundos':str_segundos}
    
    response = HttpResponse(content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['Connection'] = 'keep-alive'
    response['Transfer-Encoding'] = 'chunked'
    try:
        data = arreglo_html
        if data is not None:
            event_data = f"data: {json.dumps(data)}\n\n"
            response.write(event_data)
            response.flush()
    except GeneratorExit:  # El cliente se desconecta
        pass
    return response
    # return(HttpResponse(arreglo_html, content_type="text/event-stream"))