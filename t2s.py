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

        tts1 = gTTS(self.msg, lang='es-us', slow=False)
        tts1.save('file.mp3')
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
            self.cabello = person['faceAttributes']['hair']['hairColor'][0]['color']
            self.gafas = person['faceAttributes']['glasses']

            print(self.nombre, self.edad, self.genero, self.cabello, self.gafas)

            self.nina = ['Hermosa', 'Linda', 'Preciosa']
            self.nino = ['Campeon', 'muy Lindo', 'muy Hermoso']
            self.anos = ['Calculo en mi mente ',
                         'Puedo Ver y pienso', 'Puedo observar']
            self.despedida = ['Fue agradable conocerte. En una proxima ocasion espero verte',
                              'Sin duda eres genial, me encanto saludarte', 'Eres muy amable y agradable, me ha encantado conocerte']
            if (self.gafas != 'NoGlasses'):
                self.lentes = 'Me encantan tus Lentes'
            if (self.genero == 'female'):
                self.gene = 'una princesa'
                self.ternura = self.nina[randint(0, 2)]
            if (self.genero == 'male'):
                self.gene = 'un hombresito'
                self.ternura = self.nino[randint(0, 2)]
            self.msg = 'Hola ' + self.nombre + ', Es un placer saludarte. ' + ' Eres ' + self.gene + ' ' + self.ternura + '. Vengo junto con mis amigos de Unimagdalena.  ' + \
                self.anos[randint(0, 2)] + ' que tienes unos ' + str(int(self.edad)
                                                                     ) + ' anos de edad. ' + self.despedida[randint(0, 2)]
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
