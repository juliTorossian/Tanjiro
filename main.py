import serial, time, sys, json
from misc.perfiles import getComandosPerfil
from funciones.teclas.teclado import ejecutarMacro, escribir
from funciones.audio.audio import reproducir

cRow, cCol = 0, 0
info = False
codificacion = sys.getdefaultencoding()
teclado = [["A","B","C","D"],["E","F","G","H"],["I","J","K","L"]]
comandos = getComandosPerfil('PERFIL1')

# creo la coneccion serial al puerto 'COM10' y 9600 baudios
arduino = serial.Serial('COM10', 9600)

time.sleep(2)

def accionTecla(r, c):
    global teclado
    global comandos

    for comando in comandos:
        # print(c)
        # print(comando['tecla'])
        # print(teclado[r][c])
        if comando['tecla'] == teclado[r][c]:
            print(comando)

            if comando['comando'] == 'macro':
                ejecutarMacro(comando['parametros'])
            elif comando['comando'] == 'escribir':
                escribir(comando['parametros'])
            elif comando['comando'] == 'sonido':
                reproducir(comando['parametros'])

    # print(comandos[teclado[r][c]])
def accionEncoder(sentido):
    if sentido == 1:
        print("sube volumen")
    else:
        print("baja volumen")
def accionEncoderBtn():
    print("accion btn encoder solo")
def cambioDePerfil(r, c):
    global teclado
    perfil = teclado[r][c]
    print(f"Cambio al perfil {perfil}")
    comando = "setPerfil " +perfil
    arduino.write(bytes(comando, 'latin-1'))

def procesarComunicacion(comm):
    global teclado
    comm = str(comm, 'latin-1')
    comm = comm.strip('\n')
    comm = comm.strip('\r')
    # print(comm)
    commJson = json.loads(comm)
    print(commJson)
    # print(commJson['p'])
    if ((commJson["r"] != -1) and (commJson["e"] == 0)):
        #! Pulsacion de un boton SOLO
        # print(commJson["r"])
        # print(teclado[commJson["r"]][commJson["c"]])
        accionTecla(commJson["r"], commJson["c"])
    if (commJson["g"] != 0):
        #! Giro del encoder
        accionEncoder(commJson["g"])
    if ((commJson["e"] != 0) and ((commJson["r"] == -1))):
        #! Pulsacion del encoder SOLO
        accionEncoderBtn()
    if ((commJson["e"] != 0) and ((commJson["r"] != -1))):
        #! Pulsacion del encoder y un boton
        cambioDePerfil(commJson["r"], commJson["c"])
    


def obtenerInfoArduino():
    global info
    comando = b"getInfo"
    arduino.write(comando)
    # time.sleep(2)
    # print(arduino.readline())
    info = True

while(True):
    # if not info:
    #     obtenerInfoArduino()
    

    rawString = arduino.readline()
    procesarComunicacion(rawString)

