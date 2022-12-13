from cgi import print_arguments
from django.shortcuts import render
from django.views.generic import View
from core.models import *
from bestoff.views import propiedades
from funcionespy import *
from bestoff.forms import *

UF=34500 #CAMBIAR UF ACÁ

def propiedades_inicio(request):
    propiedades = Propiedad.objects.all()
    context={ 
        'propiedades': propiedades
    }
    return render(request, 'propiedades/index.html', context)

def propiedades_detalles(request, id, slug):
    propiedades= Propiedad.objects.filter(id=id)
    ofertas=Oferta.objects.filter(propiedad__id=id).order_by('-fecha')[:2]
    todas_ofertas=Oferta.objects.filter(propiedad__id=id).order_by('-fecha')
    rentabilidad_max= float(f'{((propiedades[0].arriendo_maximo*12)/(propiedades[0].precio*UF)*100):.1f}') 
    rentabilidad_min= float(f'{((propiedades[0].arriendo_minimo*12)/(propiedades[0].precio*UF)*100):.1f}')
    rentabilidad_real= float(f'{((propiedades[0].arriendo_actual*12)/(propiedades[0].precio*UF)*100):.1f}')
    Utilidad= float(f'{((propiedades[0].tasacion_comercial*100/propiedades[0].precio)-100):.1f}')
    images = Image.objects.all()
    documentos= Documentos_Legales.objects.all()
    if request.method == 'POST':
        form_contacto=formulario_contacto(request.POST)
        form_contacto_oferta=formulario_contacto_oferta(request.POST)
        if form_contacto_oferta.is_valid():
            data = form_contacto_oferta.cleaned_data
            save_comprador=Comprador()
            save_comprador.nombre=data['nombre']
            save_comprador.apellido=''
            save_comprador.rut=''
            save_comprador.telefono_contacto=data['telefono']
            save_comprador.save()
            save_oferta = Oferta()
            save_oferta.monto = data['monto']
            save_oferta.propiedad=propiedades[0]
            save_oferta.comprador = Comprador.objects.last()
            save_oferta.estado = 'Pendiente'
            save_oferta.save()
            form_contacto = formulario_contacto()
    else:
        form_contacto= formulario_contacto()
        form_contacto_oferta=formulario_contacto_oferta()

    context={ 
        'id': id, 
        'propiedades': propiedades,
        'images': images,
        'documentos':documentos,
        'form_contacto': form_contacto,
        'form_contacto_oferta': form_contacto_oferta,
        'rentabilidad_max': rentabilidad_max,
        'rentabilidad_min': rentabilidad_min,
        'rentabilidad_real': rentabilidad_real,
        'utilidad': Utilidad, 
        'ofertas':ofertas, 
        'todas_ofertas':todas_ofertas
    }

    return render(request, 'propiedades/detalles.html', context )

def buscador(request):
    arreglo=request.GET.get('buscar').split('-')
    propiedades= Propiedad.objects.filter(comuna__comuna__icontains=comuna_sinacentos(arreglo[0].strip()), precio__lte=arreglo[1] )
    images = Image.objects.all()
    rentabilidades=[]
    rentabilidades.append({})
    plusvalias=[]
    plusvalias.append({})
    for propiedad in propiedades:
        rentabilidades[0][propiedad.id]=float(f'{((propiedad.arriendo_actual*12)/(propiedad.precio*UF)*100):.1f}')
        plusvalias[0][propiedad.id]= float(f'{((1-(propiedad.precio/propiedad.tasacion_comercial))*100):.1f}')
    return render(request, 'propiedades/buscador.html', {'propiedades': propiedades, 'images': images, 'Comuna': arreglo[0], 'precio_max':arreglo[1], 'rentabilidad':arreglo[2], 'plusvalia':arreglo[3], 'bancaria':arreglo[4], 'rentabilidades':rentabilidades, 'plusvalias': plusvalias})

def grilla_ciudades(request, ciudad):
    if ciudad=='santiago':
        comunas=['santiago','cerrillos', 'la reina', 'las condes', 'lo barnechea', 'lo espejo', 'lo prado', 'macul', 'maipu', 'nunoa', 'pedro aguirre cerda', 'peñalolen', 'providencia', 'pudahuel', 'quilicura', 'quinta normal', 'recoleta', 'renca', 'san joaquin', 'san miguel', 'san ramon', 'vitacura']
    elif ciudad=='valparaiso':
        comunas=['valparaiso', 'viña del mar','concon', 'quilpue', 'villa alemana']
    elif ciudad=='concepcion':
        comunas=['concepcion', 'talcahuano', 'chiguayante', 'san pedro de la paz', 'penco']
    
    count=0
    for comuna in comunas:
        if count==0:
            propiedades = Propiedad.objects.filter(comuna__comuna__icontains=comuna)
        else:
            propiedades = propiedades | Propiedad.objects.filter(comuna__comuna__icontains=comuna)
        count=count+1

    images = Image.objects.all()
    return render(request, 'propiedades/grilla_ciudades.html', {'propiedades': propiedades, 'images': images, 'ciudad': ciudad.capitalize()})