# -*-coding: utf-8-*-
from gtts import gTTS
from random import randint
import os
import threading


class t2s:
    def __init__(self):
        self.state = 0
        self.file = ''
        self.msg = None

    def speaker(self):
        tts1 = gTTS(self.msg.decode("utf8"), lang='es-us', slow=False)
        with open(self.file, "wb") as archivo:
            tts1.write_to_fp(archivo)
        #tts1.save('file.mp3')
        os.system("mpg123 " + self.file)
        self.state = 0 
        

    def play(self, person):
        self.file = "file.mp3"
        if (self.state == 0):
            self.state = 1
            self.file = "file.mp3"
            self.nombre = person.get('name')
            self.edad = person['faceAttributes']['age']
            self.genero = person['faceAttributes']['gender']
            # self.cabello = person['faceAttributes']['hair']['hairColor'][0]['color']
            self.gafas = person['faceAttributes']['glasses']

            print(self.nombre, self.edad, self.genero, self.gafas)
            
            self.saludo = ['Es un placer saludarte', 'estoy feliz de estar aquí', 'me gusta estar rodeada de personas, es bueno', 'se siente bien este lugar, es especial estar aqui']
            self.lentes = ['¡uou!, me encantan tus lentes', 'tus lentes son cuul']
            self.nolentes = ['veo que no usas lentes', 'tienes lindos ojos']
            self.nina = ['Hermosa', 'Linda', 'Preciosa']
            self.senora = ['encantadora', 'feliz', 'amigable']
            self.nino = ['Campeón', 'muy Lindo', 'muy Hermoso']
            self.senor = ['simpatico', 'alegre', 'agradable']
            self.anos = ['Calculo en mi mente que ', 'Puedo Ver y pienso que ', 'Puedo observar que ', 'Estoy procesando tu edad y ']
            self.despedida = ['Fue agradable conocerte. En una próxima ocasión espero verte. ¡Adios!', 'Sin duda eres genial, me encantó saludarte. ¡Chao!', 'Eres muy amable y agradable, me ha encantado conocerte. ¡Chao!', 'conocerte ha sido increible, gracias por compartir conmigo. ¡Adios!', 'Estár aquí me gusta, pero no me puedo quedar mucho. espero volver. ¡Chao!']

            if (self.gafas != 'NoGlasses'):
                self.dlentes = self.lentes[randint(0, 1)]
            else:
                self.dlentes = self.nolentes[randint(0, 1)]
            if (self.genero == 'female'):
                if (self.edad <= 20):
                    self.gene = 'una princesa '
                    self.ternura = self.nina[randint(0, 3)]
                else:
                    self.gene = 'una seniorita '
                    self.ternura = self.senora[randint(0, 2)]
            if (self.genero == 'male'):
                if (self.edad <= 20):
                    self.gene = 'un hombresito '
                    self.ternura = self.nino[randint(0, 2)]
                else:
                    self.gene = 'un senior '
                    self.ternura = self.senor[randint(0, 2)]

            self.msg = '¡Hola ' + self.nombre + '!. ' + self.saludo[randint(0, 3)] + ' Eres ' + self.gene + ' ' + self.ternura + '. Vengo junto con mis amigos de Unimagdalena.  ' +  self.anos[randint(0, 3)] + ' tienes unos ' + str(int(self.edad)) + ' anios de edad. ' + self.dlentes + '.  ' + self.despedida[randint(0, 4)]


            print self.msg

            #tts2 = gTTS(self.anos[randint(0, 2)], 'que tienes unos ', self.edad, 'años de edad', lang='es-us', slow=False)
            #tts3 = gTTS('', self.lentes, '', self.despedida[randint(0, 2)], lang='es-us', slow=False)
            # with open(file, "wb") as archivo:
            #    tts1.write_to_fp(archivo)
            # tts2.write_to_fp(archivo)
            # tts3.write_to_fp(archivo)
            hilo2 = threading.Thread(target=self.speaker)
            hilo2.daemon = True
            hilo2.start()
