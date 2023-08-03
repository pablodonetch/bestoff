from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils import timezone
from django.shortcuts import reverse
from django.conf import settings
#from autoslug import AutoSlugField
from datetime import datetime
import os
from django.contrib.auth.models import User

class Corredor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Corredor'
        verbose_name_plural = 'Corredores'


class moneda(models.Model):
    moneda= models.CharField(max_length=100)
    def __str__(self):
        return self.moneda


class moneda_arriendo_actual(models.Model):
    moneda= models.CharField(max_length=100)
    def __str__(self):
        return self.moneda


class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    telefono_contacto= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class Comprador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    telefono_contacto= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta:
        verbose_name = 'Comprador'
        verbose_name_plural = 'Compradores'


class Estado_Oferta(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Oferta(models.Model):
    monto=models.IntegerField()
    moneda=models.ForeignKey(moneda, on_delete=models.CASCADE, default=1)
    forma_pago=models.CharField(max_length=150, default='Crédito Hipotecario')
    propiedad=models.ForeignKey('Propiedad', on_delete=models.CASCADE)
    comprador=models.ForeignKey('Comprador', on_delete=models.CASCADE)
    estado=models.ForeignKey('Estado_Oferta', on_delete=models.CASCADE, default=1)
    aceptada=models.BooleanField(default=False)
    fecha=models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'


class Contactos(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    mensaje=models.TextField()
    fecha=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


class tipo_propiedad(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.tipo}"
    class Meta:
        verbose_name = 'Tipo de Propiedad'
        verbose_name_plural = 'Tipos de Propiedades'


class tipo_operacion(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.tipo}"
    class Meta:
        verbose_name = 'Tipo de Operacion'
        verbose_name_plural = 'Tipos de Operaciones'


class comuna(models.Model):
    id = models.IntegerField(primary_key=True)
    comuna = models.CharField(max_length=50)
    provincia_id = models.IntegerField()
    def __str__(self):
        return f"{self.comuna}"
    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'


class provincias(models.Model):
    id = models.IntegerField(primary_key=True)
    provincia = models.CharField(max_length=50)
    region_id = models.IntegerField()
    def __str__(self):
        return f"{self.provincia}"
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


class regiones(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.region}"
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'


#entrega nombre en timestamp + extension del archivo
def nombre_timestamp(filename):
    fecha=datetime.now()
    nombre=f"{datetime.timestamp(fecha)}{os.path.splitext(str(filename))[1]}"
    return nombre


# Guarda en la carpeta media/propiedades las imagenes y videos de las propiedades
def user_directory_path(instance, filename):
    return 'propiedades/{0}/{1}'.format(instance.id_propiedades, nombre_timestamp(filename))


def normalice(value):
    normalice= str(value).replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").replace(" ", "-").replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U").replace("Ñ", "N")
    return normalice


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    id_propiedades= models.ForeignKey('Propiedad', on_delete=models.CASCADE, related_name='images')
    default= models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id_propiedades} {self.image}"


class Documentos_Legales(models.Model):
    documento = models.FileField(upload_to=user_directory_path)
    titulo= models.CharField(max_length=200)
    id_propiedades= models.ForeignKey('Propiedad', on_delete=models.CASCADE, related_name='documentos')
    def __str__(self):
        return f"{self.id_propiedades} {self.documento}"
    class Meta:
        verbose_name = 'Documento Legal'
        verbose_name_plural = 'Documentos Legales'


class Estado_Ocupacion(models.Model):
    estado = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.estado}"
    class Meta:
        verbose_name = 'Estado de Ocupacion'
        verbose_name_plural = 'Estados de Ocupacion'


class metodo_pago(models.Model):
    metodo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.metodo}"
    class Meta:
        verbose_name = 'Metodo de Pago'
        verbose_name_plural = 'Metodos de Pago'


class Propiedad(models.Model):
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado_uso = models.TextField(default="Buen estado. Solo necesita pintura y reparaciones menores.")
    comision_venta = models.TextField(max_length=200, default="2% + IVA del valor de venta (con Factura Excenta)")
    rol = models.CharField(max_length=50)
    tipo_propiedad = models.ForeignKey(tipo_propiedad, on_delete=models.CASCADE)
    tipo_operacion = models.ForeignKey(tipo_operacion, on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)
    moneda=models.ForeignKey(moneda, on_delete=models.CASCADE)
    superficie_construida = models.FloatField(default=0)
    superficie_terraza = models.FloatField(default=0)
    superficie_terreno = models.FloatField(default=0)
    dormitorios = models.IntegerField(default=0)
    baños = models.IntegerField(default=0)
    estacionamientos = models.IntegerField(default=0)
    bodegas = models.IntegerField(default=0)
    gastos_comunes = models.IntegerField(default=0)
    arriendo_maximo = models.IntegerField(default=0)
    arriendo_minimo = models.IntegerField(default=0)
    corredor=models.ForeignKey(Corredor, on_delete=models.CASCADE, default=1)
    estado_ocupacion = models.ForeignKey(Estado_Ocupacion, on_delete=models.CASCADE, default=1)
    arriendo_actual=models.IntegerField(default=0)
    garantia_necesaria=models.IntegerField(default=0)
    destacado=models.BooleanField(default=False)
    bestoff=models.BooleanField(default=False)
    aceptan_contado=models.BooleanField(default=True)
    aceptan_credito=models.BooleanField(default=False)
    aceptan_subsidio=models.BooleanField(default=False)
    acetan_permuta=models.BooleanField(default=False)
    aceptan_ofertas=models.BooleanField(default=False)
    propiedad_bancaria=models.BooleanField(default=False)
    video = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    youtube_video = models.CharField(verbose_name='Youtube Video (Opcional)', max_length=200, blank=True, null=True)
    imagenes = models.ManyToManyField(Image, blank=True)
    documentos_legales = models.ManyToManyField(Documentos_Legales, blank=True)
    published= models.DateTimeField(default=timezone.now)
    contribuciones=models.IntegerField(default=0)
    tasacion_fiscal=models.IntegerField(default=0)
    tasacion_comercial=models.IntegerField(default=0)
    fecha_venta_anterior=models.DateField(blank=True, null=True)
    precio_venta_anterior=models.IntegerField(default=0, blank=True, null=True)
    slug=models.TextField(max_length=200, unique=True, blank=True, null=True)
    class Meta:
        ordering = ['-published',]
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'
    def __str__(self):
        return f"{self.id}"


class Metadata(models.Model):
    description = models.CharField(max_length=200)
    keywords = models.TextField(default='0') 
    correo= models.CharField(max_length=200)
    telefono= models.CharField(max_length=200)
    titulo= models.CharField(max_length=200)
    def __str__(self):
        return self.correo
    class Meta:
        verbose_name = 'Metadata'
        verbose_name_plural = 'Metadatas'


class UsersMetadata(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    rut=models.CharField(max_length=100, blank=True, null=True)
    comuna = models.ForeignKey(comuna, models.DO_NOTHING, default=1)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    garantia= models.IntegerField(default=0)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'users_metadata'
        verbose_name = 'User metadata'
        verbose_name_plural = 'User metadata'