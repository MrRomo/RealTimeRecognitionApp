from gtts import gTTS
from neural import Neural
import os

class t2s:
    def __init__(self, person):
        self.nombre = person.get('name')
        self.edad = person.get('age')
        self.genero = person.get('gender')
        self.cabello = person.get('hairColor')
        self.gafas = person.get('glasses')




    def play(self):
        
