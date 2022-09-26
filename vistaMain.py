import tkinter as tk
from tkinter import Tk, messagebox, ttk, Frame
from funciones.teclas.teclado import grabarMacro, ejecutarMacro
from vistas.frameConn import FConn
from vistas.framePerfiles import FPerfiles
from vistas.frameBotones import FBotones
from vistas.frameAction import FActions

root = Tk()
root.geometry("800x530")
root.resizable(False,False)

perfilActivo = None

# Frame de conneccion
frameConn = FConn(root)
frameConn.place(x=0,y=0,width=800,height=60)
frameConn.config(background="lightblue")

# Frame de perfiles
framePerf = FPerfiles(root)
framePerf.place(x=17, y=110,width=380, height=90)
framePerf.config(bg="lightblue")

# Frame de botones
frameBtn = FBotones(root)
frameBtn.place(x=17, y=210,width=380, height=300)
frameBtn.config(bg="lightblue")

# Frame de acciones
frameAct = FActions(root)
frameAct.place(x=400, y=110,width=380, height=400)
frameAct.config(bg="lightblue")


def cambioDePerfil(event):
    perfilActivo = framePerf.cbPerf.get()
    frameBtn.setBotones(perfilActivo)
    frameAct.setPerfil(perfilActivo)
    # print(perfilActivo)

def cambioDeTecla(event):
    teclaActiva = frameBtn.teclaActiva
    frameAct.setBtn(teclaActiva)
    # print(teclaActiva)

def cambioDeAccion(event):
    accionSel = frameAct.cbAcciones.get()
    frameAct.setAccion(accionSel)
    # print(accionSel)

framePerf.cbPerf.bind("<<ComboboxSelected>>", cambioDePerfil)
frameBtn.lTeclaActiva.bind("<Configure>", cambioDeTecla)
frameAct.cbAcciones.bind("<<ComboboxSelected>>", cambioDeAccion)


root.mainloop()
