from re import sub
from misc.perfiles import getComando
from misc.param import getPerfilPre
from funciones.teclas.teclado import ejecutarMacro, escribir
from funciones.audio.volumen import subirVolumen, bajarVolumen

perfilPredefinido = getPerfilPre()
perfilActivo = ''

def setPefil(perfilParam):
    global perfilActivo
    perfilActivo = perfilParam

def getPerfilActivo():
    global perfilActivo
    return perfilActivo if len(perfilActivo) > 0 else perfilPredefinido


def accionTecla(tecla):
    perfil = getPerfilActivo()
    comando, param = getComando(perfil=perfil, tecla=tecla)

    print(comando)
    print(param)

    if comando == 'macro':
        ejecutarMacro(param)
    elif comando == 'escribir':
        escribir(param)
    elif comando == 'sonido':
        # reproducir(param)
        pass

def accionEncoder(sentido):
    if sentido == 1:
        print("sube volumen")
        subirVolumen(proceso="Spotify.exe", decibels=0.05)
    else:
        print("baja volumen")
        bajarVolumen(proceso="Spotify.exe", decibels=0.05)

def accionEncoderBtn():
    print("accion btn encoder solo")

def cambioDePerfil(tecla):
    global teclado
    perfil = tecla
    print(f"Cambio al perfil {perfil}")
    comando = "setPerfil " +perfil
    # arduino.write(bytes(comando, 'latin-1'))