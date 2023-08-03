from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from .models import Notificaciones



class WSConsumer(WebsocketConsumer):
	
	def connect(self):
		self.accept()
		
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
		"""
		for i in range(1000):
			self.send(json.dumps({'message': randint(1, 1000)}))
			sleep(1)
		"""	