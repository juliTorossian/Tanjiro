from vistaMain import VentanaMain
import threading
from tecladoEjecucion import escuchar, stop


ventana = VentanaMain()

def seCierraLaVentana():
    # print('stop 1')
    stop()
    ventana.ventana.destroy()

def main():

    th_test = threading.Thread(target=escuchar, args=())
    th_test.start()

    ventana.ventana.protocol("WM_DELETE_WINDOW", seCierraLaVentana)
    ventana.ventana.mainloop()

if '__main__' == __name__:
    main()
