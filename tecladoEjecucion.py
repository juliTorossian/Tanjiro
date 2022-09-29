import threading
import ctypes
from misc.arduino import Arduino
from misc.acciones import accionTecla, accionEncoder, accionEncoderBtn, cambioDePerfil
from misc.param import getCOMParam

puertoCOM = getCOMParam()
puerto = None
stop = False
connOk = False

id_thread = None

def ejecutar():
    global connOk
    global id_thread
    th_test = threading.Thread(target=escuchar, args=())
    th_test.start()
    id_thread = th_test.ident
    print(id_thread)

def escuchar():
    global stop
    stop = False
    global puerto
    global puertoCOM
    global connOk

    try:
        puerto = puerto if not puerto == None else puertoCOM
        arduino = Arduino(puerto=puerto)
        connOk = True

        while(stop != True):
            aux = arduino.leerSerial()
            if aux != None:
                print(aux)
                # print(aux['accion'])
                if aux['accion'] == 'tecla':
                    accionTecla(aux['param1'])
                elif aux['accion'] == 'encoderGiro':
                    accionEncoder(aux['param1'])
                elif aux['accion'] == 'encoderBtn':
                    accionEncoderBtn(aux['param1'])
                elif aux['accion'] == 'teclaEncoder':
                    cambioDePerfil(aux['param1'])
            
            # if stop == True:
            #     raise Exception('Se detuvo la escucha')

    except Exception as e:
        print(e)
        connOk = False
        # raise ArduinoConnException('error de con')

def stop():
    global stop
    global id_thread

    ctypes.pythonapi.PyThreadState_SetAsyncExc(id_thread, 0)

    print('se detubo la escucha')
    stop = True
def setPuerto(puertoAct):
    global puerto
    puerto = puertoAct

        