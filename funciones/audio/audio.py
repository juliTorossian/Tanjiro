from playsound import playsound
import os

def reproducir(path):
    print(path)
    playsound(path)


print(os.path.dirname(__file__))
print('inicio')
playsound(f"{os.path.dirname(__file__)}\\Test-Sonido_01.mp3")
print('termino')