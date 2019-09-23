# -*- coding: utf-8 -*-

from gtts import gTTS
import os

file = "file2.mp3"

tts1 = gTTS('Insertar característica 1', lang='es-us', slow=False)
tts2 = gTTS('Insertar característica 2', lang='es-us', slow=False)

with open(file, "wb") as archivo:
    tts1.write_to_fp(archivo)
    tts2.write_to_fp(archivo)

os.system("mpg123 " + file)
