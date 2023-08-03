from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from .models import Notificaciones
from datetime import datetime, timedelta


class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		propiedades= Propiedad.objects.all()
		propiedades_diccionario=defaultdict(dict)
		for i in range(0,propiedades.count()):
			propiedades_diccionario_socket[propiedades[i].id]['tiempo_remanente']=propiedades[i].comuna.comuna
			ahora = datetime.now()
			tiempo_restante = propiedades[i].fecha_termino - ahora
			propiedades_diccionario_socket[propiedades[i].id]['dias']=tiempo_restante.days
			propiedades_diccionario_socket[propiedades[i].id]['horas'],propiedades_diccionario[propiedades[i].id]['segundos']=divmod(tiempo_restante.seconds, 3600)
			propiedades_diccionario_socket[propiedades[i].id]['minutos'],propiedades_diccionario[propiedades[i].id]['segundos']=divmod(segundos, 60)
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