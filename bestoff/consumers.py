from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
from datetime import datetime, timedelta
from core.models import *

class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		self.propiedad_id = self.scope['url_route']['kwargs']['propiedad_id']
		try:
			self.propiedad = Propiedad.objects.get(id=self.propiedad_id)
		except self.propiedad.DoesNotExist:
			# Si el producto no existe, cierra la conexión.
			self.close()
		propiedad_diccionario_socket={}
		#calulamos el tiempo restante
		ahora = datetime.now()
		# Convertir a objetos naive
		ahora_naive = ahora.replace(tzinfo=None)
		termino_naive = self.propiedad.fecha_termino.replace(tzinfo=None)
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
		# print('id_propiedad: dias ' + str(dias) + ' ;horas ' + str(horas)+' segundos: '+str(segundos))
		propiedad_diccionario_socket={'dias':str_dias,'horas':str_horas,'minutos':str_minutos,'segundos':str_segundos}
		self.send(text_data=json.dumps(arreglo_html))