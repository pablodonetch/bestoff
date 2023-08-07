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
        cuenta_regresiva = str(dias) + ':' + str(horas)+':'+str(minutos)+':'+str(segundos)
        # print('id_propiedad: dias ' + str(dias) + ' ;horas ' + str(horas)+' segundos: '+str(segundos))
        propiedad_diccionario_socket={'dias':dias,'horas':horas,'minutos':minutos,'segundos':segundos}
        self.send(text_data=json.dumps(cuenta_regresiva))