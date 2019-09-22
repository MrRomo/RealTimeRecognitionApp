from gtts import gTTS
import os

file = "file.mp3"
tts = gTTS('Aura. Me alegro que estes viendo peliculas. . . Yo estoy aqui programando', lang='es-us', slow=False)

with open(file, "wb") as archivo:
    tts.write_to_fp(archivo)

os.system("mpg123 " + file)
