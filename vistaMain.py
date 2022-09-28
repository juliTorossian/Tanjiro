import tkinter as tk
from tkinter import Tk, messagebox, ttk, Frame
from funciones.teclas.teclado import grabarMacro, ejecutarMacro
from vistas.frameConn import FConn
from vistas.framePerfiles import FPerfiles
from vistas.frameBotones import FBotones
from vistas.frameAction import FActions

class VentanaMain():
    
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        window_width = 800
        window_height = 530
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.ventana.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.perfilActivo = None

        self.crearVentanas()
        self.bindeos()


    def crearVentanas(self):
        # Frame de conneccion
        self.frameConn = FConn(self.ventana)
        self.frameConn.place(x=0,y=0,width=800,height=60)
        self.frameConn.config(background="lightblue")

        # Frame de perfiles
        self.framePerf = FPerfiles(self.ventana)
        self.framePerf.place(x=17, y=110,width=380, height=90)
        self.framePerf.config(bg="lightblue")

        # Frame de botones
        self.frameBtn = FBotones(self.ventana)
        self.frameBtn.place(x=17, y=210,width=380, height=300)
        self.frameBtn.config(bg="lightblue")

        # Frame de acciones
        self.frameAct = FActions(self.ventana)
        self.frameAct.place(x=400, y=110,width=380, height=400)
        self.frameAct.config(bg="lightblue")


    def cambioDePerfil(self, event):
        perfilActivo = self.framePerf.cbPerf.get()
        self.frameBtn.setBotones(perfilActivo)
        self.frameAct.setPerfil(perfilActivo)
        # print(perfilActivo)

    def cambioDeTecla(self, event):
        teclaActiva = self.frameBtn.teclaActiva
        self.frameAct.setBtn(teclaActiva)
        # print(teclaActiva)

    def cambioDeAccion(self, event):
        accionSel = self.frameAct.cbAcciones.get()
        self.frameAct.setAccion(accionSel)
        # print(accionSel)

    def bindeos(self):
        self.framePerf.cbPerf.bind("<<ComboboxSelected>>", self.cambioDePerfil)
        self.frameBtn.lTeclaActiva.bind("<Configure>", self.cambioDeTecla)
        self.frameAct.cbAcciones.bind("<<ComboboxSelected>>", self.cambioDeAccion)



# root.mainloop()
