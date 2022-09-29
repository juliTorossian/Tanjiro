from excepciones.excepciones import ArduinoConnException
import serial
import json

baudrate = 9600
teclado = [["A","B","C","D"],["E","F","G","H"],["I","J","K","L"]]


class Arduino:

    def __init__(self, puerto) -> None:
        self.puerto = puerto
        self.conn   = self.connArduino()

    def connArduino(self):
        try:
            return serial.Serial(self.puerto, baudrate)
        except:
            raise ArduinoConnException(f"Error al conectar al puerto {self.puerto}")

    def obtenerInfoArduino(self):
        comando = b"getInfo"
        self.conn.write(comando)

    def procesarComunicacion(self, comm):
        global teclado

        comm = str(comm, 'latin-1')
        comm = comm.strip('\n')
        comm = comm.strip('\r')
        # print(comm)
        commJson = json.loads(comm)
        print(commJson)
        if ((commJson["r"] != -1) and (commJson["e"] == 0)):
            #! Pulsacion de un boton SOLO
            # print(commJson["r"])
            # print(teclado[commJson["r"]][commJson["c"]])
            # accionTecla(commJson["r"], commJson["c"])
            return {"accion":"tecla", "param1":teclado[commJson["r"]][commJson["c"]]}
        if (commJson["g"] != 0):
            #! Giro del encoder
            # accionEncoder(commJson["g"])
            return {"accion":"encoderGiro", "param1":commJson["g"], "param2":""}
        if ((commJson["e"] != 0) and ((commJson["r"] == -1))):
            #! Pulsacion del encoder SOLO
            return {"accion":"encoderBtn", "param1":True, "param2":""}
            # accionEncoderBtn()
        if ((commJson["e"] != 0) and ((commJson["r"] != -1))):
            #! Pulsacion del encoder y un boton
            return {"accion":"teclaEncoder", "param1":teclado[commJson["r"]][commJson["c"]]}
            # cambioDePerfil(commJson["r"], commJson["c"])

    def leerSerial(self):
        rawString = self.conn.readline()
        return self.procesarComunicacion(rawString)