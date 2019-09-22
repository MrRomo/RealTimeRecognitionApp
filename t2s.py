from gtts import gTTS
import os

file = "file.mp3"

tts1 = gTTS('Insertar caracteristica 1', lang='es-us', slow=False)
tts2 = gTTS('Insertar caracteristica 2', lang='es-us', slow=False)

with open(file, "wb") as archivo:
    tts1.write_to_fp(archivo)
    tts2.write_to_fp(archivo)

os.system("mpg123 " + file)
