#-*-coding: utf-8-*-
from gtts import gTTS
from random import randint
import os

class t2s:
    def __init__(self):
        self.state = 0

    def play(self, person):
        if (self.state == 0):
            self.state = 1
            self.file = "file.mp3"
            self.nombre = person.get('name')
            self.edad = person.get('age')
            self.genero = person.get('gender')
            self.cabello = person.get('hairColor')
            self.gafas = person.get('glasses')

            self.nina = ['Hermosa', 'Linda', 'Preciosa']
            self.nino = ['Campeon', 'muy Lindo', 'muy Hermoso']
            self.anos = ['Calculo en mi mente ', 'Puedo Ver y pienso', 'Puedo observar']
            self.despedida = ['Fue agradable conocerte. En una proxima ocasion espero verte', 'Sin duda eres genial, me encanto saludarte', 'Eres muy amable y agradable, me ha encantado conocerte']
            if (self.gafas != 'NoGlasses'):
                self.lentes = 'Me encantan tus Lentes'
            if (self.genero == 'Female'):
                self.gene = 'una niña'
                self.ternura = self.nina[randint(0, 2)]
            if (self.genero == 'Male'):
                self.gene = 'un niño'
                self.ternura = self.nino[randint(0, 2)]

            tts1 = gTTS('Hola ', self.nombre, 'Es un placer saludarte.', 'Eres ', self.gene, self.ternura, 'Vengo con mis amigos de Unimagdalena', lang='es-us', slow=False)
            tts2 = gTTS(self.anos[randint(0, 2)], 'que tienes unos ', self.edad, 'años de edad', lang='es-us', slow=False)
            tts3 = gTTS('', self.lentes, '', self.despedida[randint(0, 2)], lang='es-us', slow=False)
            with open(file, "wb") as archivo:
                tts.write_to_fp(archivo)
            os.system("mpg123 " + file)
            self.state = 0
