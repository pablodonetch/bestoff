from cgi import print_arguments
from django.shortcuts import render
from django.views.generic import View
from core.models import *
from bestoff.views import propiedades

def propiedades_inicio(request):
    propiedades = Propiedad.objects.all()
    context={ 
        'propiedades': propiedades
    }
    return render(request, 'propiedades/index.html', context)


def santiago (request):
    propiedades = Propiedad.objects.all()
    context={ 
        'propiedades': propiedades
    }
    return render(request, 'propiedades/santiago.html', context)

def valparaiso (request):
    propiedades = Propiedad.objects.all()
    context={ 
        'propiedades': propiedades
    }
    return render(request, 'propiedades/valparaiso.html', context)


def concepcion (request):
    propiedades = Propiedad.objects.all()
    context={ 
        'propiedades': propiedades
    }
    return render(request, 'propiedades/concepcion.html', context)


def propiedades_detalles(request, id, slug):
    ''''
    propiedad = Propiedad.objects.filter(id=id)
    images= Image.objects.filter(id_propiedades=id)
    '''
    UF=34500
    propiedades= Propiedad.objects.filter(id=id)
    rentabilidad_max= float(f'{((propiedades[0].arriendo_maximo*12)/(propiedades[0].precio*UF)*100):.1f}') 
    rentabilidad_min= float(f'{((propiedades[0].arriendo_minimo*12)/(propiedades[0].precio*UF)*100):.1f}')
    Utilidad= float(f'{((propiedades[0].tasacion_comercial*100/propiedades[0].precio)-100):.1f}')
    print(Utilidad)
    images = Image.objects.all()
    documentos= Documentos_Legales.objects.all()
    return render(request, 'propiedades/detalles.html', {'id':id, 'propiedades': propiedades, 'images': images, 'documentos':documentos, 'rentabilidad_max': rentabilidad_max, 'rentabilidad_min': rentabilidad_min, 'utilidad': Utilidad})


def buscador(request):
    arreglo=request.GET.get('buscar')
    #resultado= Propiedad.objects.get(direccion__icontains=arreglo)
    propiedades= Propiedad.objects.filter(slug__icontains=arreglo)
    images = Image.objects.all()
    return render(request, 'propiedades/buscador.html', {'propiedades': propiedades, 'images': images})