from django import template
from core.models import *
import math
from django.template.defaulttags import register

register = template.Library()

#######Métodos de bases de datos


@register.filter(name='getMetadata')
def getMetadata(n):
    datos=Metadata.objects.get()
    lista=[datos.keyword, datos.description, datos.correo, datos.telefono, datos.titulo]
    if n==1:
        return datos.keyword
    if n==2:
        return datos.description
    if n==3:
        return datos.correo
    if n==4:
        return datos.telefono
    if n==5:
        return datos.titulo


@register.filter
def accede_diccionario(dictionary, key):
    return dictionary.get(key)


#######Métodos de formateo
@register.filter(name="ejemploFiltro")
def ejemploFiltro(parametro):
	return f"el valor de parámetro es {parametro}"


@register.filter(name='numberFormatFloat')
def numberFormatFloat(numero):
    if numero == None:
        return 0
    elif numero ==0:
        return 0
    else:
        numero=float(numero)
        return "{:,}".format(numero).replace(".",",")[:-1]

@register.filter(name='numberFormatInt')
def numberFormatInt(numero):
    if numero == None:
        return 0
    else:
        numero=float(numero)
        return "{:,}".format(numero).replace(",",".")[:-2]

@register.filter(name='truncDecimal')
def numberFormat(numero):
    if numero == None:
        return 0
    else:
        return math.trunc(numero)

@register.filter(name='invierteFecha')
def invierteFecha(fechaDateTime):
    fecha = fechaDateTime.strftime('%d/%m/%Y')
    return fecha


@register.filter(name='invierteFechaHora')
def invierteFechaHora(fechaDateTime):
    fecha = fechaDateTime.strftime('%d-%m-%Y %H:%M:%S')
    return fecha