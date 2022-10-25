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
    propiedades = Propiedad.objects.all()
    images = Image.objects.all()
    context={ 
        'propiedades': propiedades,
        'images': images,
    }
    return render(request, 'propiedades/detalles.html', {'id':id, 'propiedades': propiedades, 'images': images})


def buscador(request):
    arreglo=request.GET.get('buscar')
    #resultado= Propiedad.objects.get(direccion__icontains=arreglo)
    propiedades= Propiedad.objects.filter(slug__icontains=arreglo)
    images = Image.objects.all()
    return render(request, 'propiedades/buscador.html', {'propiedades': propiedades, 'images': images})