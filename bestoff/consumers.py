from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from .models import Notificaciones
from datetime import datetime, timedelta

class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		self.producto_id = self.scope['url_route']['kwargs']['propiedad_id']
		try:
			self.propiedad = Propiedad.objects.get(id=self.propiedad_id)
		except Producto.DoesNotExist:
			# Si el producto no existe, cierra la conexión.
			self.close()
		propiedad_diccionario_socket={}
		#calulamos el tiempo restante
		ahora = datetime.now()
		tiempo_restante = self.propiedad.fecha_termino - ahora
		dias=tiempo_restante.days
		horas,segundos=divmod(tiempo_restante.seconds, 3600)
		minutos,segundos=divmod(segundos, 60)
		propiedad_diccionario_socket={'dias':dias,'horas':horas,'minutos':minutos,'segundos':segundo}
		self.send(json.dumps({'propiedades_diccionario_socket': propiedades_diccionario_socket}))
		"""
		notificaciones=Notificaciones.objects.filter(tipo=0).all()
		texto=""
		if len(notificaciones) == 0:
			self.send(json.dumps({'message': 'no hay mensajes'}))
			sleep(1)
		else:
			for notificacione in notificaciones:
				texto=f"{texto} {notificacione.titulo} | {notificacione.mensaje}<br/>"
				#texto=f"{texto} {notificacione.titulo} {len(notificaciones)}<br/>"
				self.send(json.dumps({'message': texto}))
				sleep(1)
		
		for i in range(1000):
			self.send(json.dumps({'message': randint(1, 1000)}))
			sleep(1)
		"""	