from misc.perfiles import getComando
from misc.param import getPerfilPre
from funciones.teclas.teclado import ejecutarMacro, escribir

perfilPredefinido = getPerfilPre()

def accionTecla(tecla):
    comando, param = getComando(perfil=perfilPredefinido, tecla=tecla)

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
    else:
        print("baja volumen")

def accionEncoderBtn():
    print("accion btn encoder solo")

def cambioDePerfil(tecla):
    global teclado
    perfil = tecla
    print(f"Cambio al perfil {perfil}")
    comando = "setPerfil " +perfil
    # arduino.write(bytes(comando, 'latin-1'))