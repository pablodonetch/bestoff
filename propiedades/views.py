from cgi import print_arguments
from django.shortcuts import render
from django.views.generic import View
from core.models import *
from bestoff.views import propiedades
from funcionespy import *
from bestoff.forms import *
from math import ceil
from collections import defaultdict

UF=35200 #CAMBIAR UF ACÁ
tasa_hip_inicial=0.045

def propiedades_inicio(request):
    propiedades = Propiedad.objects.all()
    context={ 
        'propiedades': propiedades
    }
    return render(request, 'propiedades/index.html', context)

def propiedades_detalles(request,oferta_enviada, id, slug ):
    propiedades= Propiedad.objects.filter(id=id)
    ofertas=Oferta.objects.filter(propiedad__id=id, aceptada=True).order_by('-fecha')[:2]
    todas_ofertas=Oferta.objects.filter(propiedad__id=id , aceptada=True).order_by('-fecha')
    rentabilidad_real= float(f'{((propiedades[0].arriendo_actual*12)/(propiedades[0].precio*UF)*100):.1f}')
    Utilidad= float(f'{((propiedades[0].tasacion_comercial*100/propiedades[0].precio)-100):.1f}')
    images = Image.objects.all()
    documentos= Documentos_Legales.objects.all()
    formulario_vender='0'
    costo_compra=int(propiedades[0].precio)
    pie= 20
    arriendo_esperado=float(f'{(propiedades[0].arriendo_maximo + propiedades[0].arriendo_minimo)/(UF*2):.1f}')
    tasa_hip_anual=tasa_hip_inicial
    if request.method == 'POST':
        data=request.POST
        action = data.get("enviar")
        if action=="vender":
            form_contacto=formulario_contacto(request.POST)
            form_contacto_oferta=formulario_contacto_oferta()
            form_financiero=formulario_financiero(initial={'precio_compra': costo_compra, 'pie': pie, 'tasa':str(tasa_hip_anual*100).replace('.',','), 'arriendo_esperado': str(arriendo_esperado).replace('.',',')})
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
        if action=="ofertar":
            form_contacto_oferta=formulario_contacto_oferta(request.POST)
            form_contacto = formulario_contacto()
            form_financiero=formulario_financiero(initial={'precio_compra': costo_compra, 'pie': pie, 'tasa':str(tasa_hip_anual*100).replace('.',','), 'arriendo_esperado': str(arriendo_esperado).replace('.',',')})
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
                save_oferta.estado = Estado_Oferta.objects.filter(id=2)[0]
                save_oferta.save()
                form_contacto_oferta=formulario_contacto_oferta()
                oferta_enviada='1'
        if action=="recalcular":
            form_contacto_oferta=formulario_contacto_oferta()
            form_contacto = formulario_contacto()
            form_financiero=formulario_financiero(request.POST)
            if form_financiero.is_valid():
                print('entra al recalcular valido')
                costo_compra=int(data['precio_compra'])
                pie=int(data['pie'])
                tasa_hip_anual=float(str(data['tasa']).replace(',','.'))/100
                if propiedades[0].arriendo_actual == 0:
                    arriendo_esperado=float(str(data['arriendo_esperado']).replace(',','.'))
                else:
                    arriendo_esperado=propiedades[0].arriendo_actual
    else:
        form_contacto= formulario_contacto()
        form_contacto_oferta=formulario_contacto_oferta()
        form_financiero=formulario_financiero(initial={'precio_compra': costo_compra, 'pie': pie, 'tasa':str(tasa_hip_anual*100).replace('.',','), 'arriendo_esperado': str(arriendo_esperado).replace('.',',')})
    '''Calculo de Variables financieras sin recalculo'''
    costo_estudio=10
    costo_escritura=10
    costo_notaria=5
    costo_vv=float(f'{ceil((costo_compra*UF*(pie/100))/49000000)*0.3:.1f}')
    costo_cbr=(ceil(costo_compra*0.006))
    total_costo=costo_estudio+costo_escritura+costo_notaria+costo_vv+costo_cbr
    tasacion_com=propiedades[0].tasacion_comercial
    plusvalia=tasacion_com-costo_compra-total_costo
    plusvalia_porc=int(plusvalia/costo_compra*100)
    arriendo=float(f'{propiedades[0].arriendo_actual/UF:.1f}')
    if propiedades[0].arriendo_actual == 0:
        arriendo=arriendo_esperado
    arriendo_anual=float(f'{arriendo*12:.1f}')
    comision_arriendo=float(f'{arriendo*0.07:.1f}')
    comision_arriendo_anual=float(f'{comision_arriendo*12:.1f}')
    rentabilidad_anual_c_adm=float(f'{(arriendo_anual-comision_arriendo_anual)/costo_compra*100:.1f}')
    rentabilidad_anual_s_adm=float(f'{arriendo_anual/costo_compra*100:.1f}')
    año=0
    cuotas=[]
    cuotas.append({})
    tasa_hip=tasa_hip_anual/12
    for i in range(1,7):
        pie=0.2
        año+=5
        meses=año*12 
        for j in range(1,5): 
            cuota=(tasa_hip) * (1/(1-(1+tasa_hip)**(-meses)))*(costo_compra*(1-pie))
            cuotas[0][f'{i},{j}']=float(f'{cuota:.1f}')
            #print(f'({i},{j})= año={año}, meses={meses} pie= {pie} cuota={cuota}')
            pie=float(f'{pie+0.1:.1f}')
 
    context={ 
        'id': id,
        'slug': slug,
        'propiedades': propiedades,
        'images': images,
        'documentos':documentos,
        'form_contacto': form_contacto,
        'form_contacto_oferta': form_contacto_oferta,
        'formulario_vender':formulario_vender,
        'formulario_financiero':form_financiero,
        'rentabilidad_real': rentabilidad_real,
        'utilidad': Utilidad, 
        'ofertas':ofertas, 
        'todas_ofertas':todas_ofertas,
        'oferta_enviada':oferta_enviada,
        'direccion':f'{propiedades[0].direccion}, {propiedades[0].comuna}',
        'costo_compra':costo_compra,
        'costo_estudio':costo_estudio,
        'costo_escritura':costo_escritura,
        'costo_notaria':costo_notaria,
        'costo_vv':costo_vv,
        'costo_cbr':costo_cbr,
        'total_costo':total_costo,
        'tasacion_com':tasacion_com,
        'plusvalia':plusvalia,
        'plusvalia_porc':plusvalia_porc,
        'arriendo':arriendo,
        'arriendo_anual':arriendo_anual,
        'comision_arriendo':comision_arriendo,
        'comision_arriendo_anual':comision_arriendo_anual,
        'rentabilidad_anual_c_adm':rentabilidad_anual_c_adm,
        'rentabilidad_anual_s_adm':rentabilidad_anual_s_adm,
        'cuotas':cuotas,
        'tasa_hip':tasa_hip_anual*100,
    }

    return render(request, 'propiedades/detalles.html', context )

def mejores_retornos(request):
    pass

def mejores_plusvalia(request):
    pass

def mejores_retornos_santiago(request):
    pass

def mejores_plusvalia_santiago(request):
    pass



def buscador(request):
    comuna=request.GET.get('buscar')
    contrato=request.GET.get('contrato')
    rentabilidad=request.GET.get('rentabilidad')
    plusvalia=request.GET.get('plusvalia')
    propiedades= Propiedad.objects.filter(comuna__comuna__icontains=comuna_sinacentos(comuna.strip()))
    if contrato=='true':
        propiedades= Propiedad.objects.filter(comuna__comuna__icontains=comuna_sinacentos(comuna.strip()))
    propiedades_diccionario=defaultdict(dict)
    def sort_by_rentabilidad(item):
        return item[1]['rentabilidad']
    def sort_by_plusvalia(item):
        return item[1]['plusvalia']
    for i in range(0,propiedades.count()):
        if contrato=='true' and propiedades[i].arriendo_actual>0:
            propiedades_diccionario[propiedades[i].id]['comuna']=propiedades[i].comuna.comuna
            propiedades_diccionario[propiedades[i].id]['precio']=float(f'{propiedades[i].precio}')
            propiedades_diccionario[propiedades[i].id]['rentabilidad']=(float(f'{((propiedades[i].arriendo_actual*12)/(propiedades[i].precio*UF)*100):.1f}'))
            propiedades_diccionario[propiedades[i].id]['plusvalia']=(float(f'{((propiedades[i].tasacion_comercial*100/propiedades[i].precio)-100):.1f}'))
            propiedades_diccionario[propiedades[i].id]['propiedad_bancaria']=propiedades[i].propiedad_bancaria
        if contrato=='false':
            propiedades_diccionario[propiedades[i].id]['comuna']=propiedades[i].comuna.comuna
            propiedades_diccionario[propiedades[i].id]['precio']=float(f'{propiedades[i].precio}')
            propiedades_diccionario[propiedades[i].id]['rentabilidad']=(float(f'{((propiedades[i].arriendo_actual*12)/(propiedades[i].precio*UF)*100):.1f}'))
            propiedades_diccionario[propiedades[i].id]['plusvalia']=(float(f'{((propiedades[i].tasacion_comercial*100/propiedades[i].precio)-100):.1f}'))
            propiedades_diccionario[propiedades[i].id]['propiedad_bancaria']=propiedades[i].propiedad_bancaria
    if plusvalia=='true':
        propiedades_diccionario=dict(sorted(propiedades_diccionario.items(), key=sort_by_plusvalia, reverse=True))
    if rentabilidad=='true':
        propiedades_diccionario=dict(sorted(propiedades_diccionario.items(), key=sort_by_rentabilidad, reverse=True))
    propiedades_diccionario = dict(propiedades_diccionario)
    form_buscar=formulario_buscar()
    images = Image.objects.all()
    context={
        'propiedades': propiedades, 
        'propiedades_diccionario':propiedades_diccionario,
        'images': images, 
        'Comuna': comuna,
        'contrato': contrato,
        'rentabilidad': rentabilidad,
        'plusvalia': plusvalia,
        'formulario_buscar': form_buscar,
    }
    return render(request, 'propiedades/buscador.html', context)

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

def ofertar(request, id, slug):
    form_contacto_oferta_2=formulario_contacto_oferta_2()
    propiedades= Propiedad.objects.filter(id=id)
    images=Image.objects.filter(id_propiedades__id=id)[:1]
    oferta_enviada='0'
    if request.method == 'POST':
        data=request.POST
        action = data.get("enviar")
        if action=="ofertar":
            form_contacto_oferta_2=formulario_contacto_oferta_2(request.POST)
            if form_contacto_oferta_2.is_valid():
                data = form_contacto_oferta_2.cleaned_data
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
                save_oferta.estado = Estado_Oferta.objects.filter(id=2)[0]
                save_oferta.save()
                form_contacto_oferta_2=formulario_contacto_oferta_2()
                oferta_enviada='1'
                return propiedades_detalles(request,oferta_enviada, id, slug )
            else:
                oferta_enviada='2'
    context={
        'id':id,
        'propiedades':propiedades,
        'images':images,
        'slug':slug,
        'form_contacto_oferta_2': form_contacto_oferta_2,
        'oferta_enviada':oferta_enviada,
    }
    return render(request, 'propiedades/ofertar.html', context )