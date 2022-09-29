from vistaMain import VentanaMain
from tecladoEjecucion import ejecutar, stop, connOk


ventana = VentanaMain()

def seCierraLaVentana():
    stop()
    ventana.ventana.destroy()

def main():

    ejecutar()
    print(connOk)

    ventana.ventana.protocol("WM_DELETE_WINDOW", seCierraLaVentana)
    ventana.ventana.mainloop()

if '__main__' == __name__:
    main()
