from misc.arduino import Arduino
from misc.acciones import accionTecla, accionEncoder, accionEncoderBtn, cambioDePerfil
from misc.param import getCOMParam

puertoCOM = getCOMParam()
stop = False

def escuchar():
    arduino = Arduino(puerto=puertoCOM)

    while(True):
        print('0')
        aux = arduino.leerSerial()
        if aux != None:
            print(aux)
            print(aux['accion'])
            if aux['accion'] == 'tecla':
                accionTecla(aux['param1'])
            elif aux['accion'] == 'encoderGiro':
                accionEncoder(aux['param1'])
            elif aux['accion'] == 'encoderBtn':
                accionEncoderBtn(aux['param1'])
            elif aux['accion'] == 'teclaEncoder':
                cambioDePerfil(aux['param1'])
        
        if stop:
            break

def stop():
    global stop
    print('se detubo la escucha')
    stop = True


        