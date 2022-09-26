from tkinter import ttk, Frame, messagebox
from misc.perfiles import setComando, teclaConComando

acciones = ["Macro", "Escritura", "Sonido"]

class FActions(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.perfil      = None
        self.tecla       = None
        self.fAccion     = None
        self.accionSelec = None

        self.crearVentana()

    def getTecla(self):
        return self.tecla
    def getPerfil(self):
        return self.perfil

    def setPerfil(self, perfil):
        self.perfil = perfil
        self.lPerfil.config(text="Perfil: {}".format(self.perfil))
    def setBtn(self, tecla):
        self.tecla = tecla
        self.lTecla.config(text="Tecla: {}".format(self.tecla))

    def setAccion(self, accion):

        if (self.tecla != None and self.perfil != None):
            if (accion != self.accionSelec):
                if (self.fAccion != None):
                    self.fAccion.destroy()
                
                if (accion == "Escritura"):
                    self.fAccion = fAccionEscritura(self)
                    self.fAccion.pack()
                    self.accionSelec = accion
                elif (accion == "Macro"):
                    self.fAccion = fAccionMacro(self)
                    self.fAccion.pack()
                    self.accionSelec = accion
                elif (accion == 'Sonido'):
                    self.fAccion = fAccionSonido(self)
                    self.fAccion.pack()
                    self.accionSelec = accion


    def crearVentana(self):
        self.lPerfil = ttk.Label(self, text="Perfil: {}".format(self.perfil))
        self.lPerfil.pack()
        self.lTecla = ttk.Label(self, text="Tecla: {}".format(self.tecla))
        self.lTecla.pack()

        self.cbAcciones = ttk.Combobox(self, state='readonly', values=acciones)
        self.cbAcciones.pack()
        # self.cbAcciones.bind("<<ComboboxSelected>>", self.cambioDeAccion())
        
class fAccionEscritura(Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.tecla  = master.tecla
        self.perfil = master.perfil
        self.accion = "escritura"

        self.crearVentana()

    def guardarAccion(self):

        accion = {
            "tecla": None,
            "comando": None,
            "parametro": None
        }
        # accion = '"tecla":"{0}","comando":"{1}","parametro":"{2}"'.format(self.tecla, self.accion, self.eTexto.get())
        accion["tecla"] = self.tecla
        accion["comando"] = self.accion
        accion["parametro"] = self.eTexto.get()

        if not teclaConComando:
            setComando(self.perfil, accion, False)
        else:
            respuesta=messagebox.askyesno("Tecla con comando", "Esta tecla ya tiene un comando asociado, desea remplazarlo?")
            if respuesta==True:
                setComando(self.perfil, accion, True)

        self.eTexto.config(textvariable="")

    def crearVentana(self):
        
        lAccion = ttk.Label(self, justify="center")
        lAccion.config(text="Ingrese el texto que quiere que se escriba:")
        lAccion.pack()
        self.eTexto = ttk.Entry(self)
        self.eTexto.pack()

        self.bGuardar = ttk.Button(self, text="Guardar", command=self.guardarAccion)
        self.bGuardar.pack()

class fAccionMacro(Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.tecla  = master.tecla
        self.perfil = master.perfil
        self.accion = "macro"

        self.crearVentana()

    def guardarAccion(self):

        accion = {
            "tecla": None,
            "comando": None,
            "parametro": None
        }
        # accion = '"tecla":"{0}","comando":"{1}","parametro":"{2}"'.format(self.tecla, self.accion, self.eTexto.get())
        accion["tecla"] = self.tecla
        accion["comando"] = self.accion
        accion["parametro"] = self.eTexto.get()

        if not teclaConComando:
            setComando(self.perfil, accion, False)
        else:
            respuesta=messagebox.askyesno("Tecla con comando", "Esta tecla ya tiene un comando asociado, desea remplazarlo?")
            if respuesta==True:
                setComando(self.perfil, accion, True)

        self.eTexto.config(textvariable="")

    def crearVentana(self):
        
        lAccion = ttk.Label(self, justify="center")
        lAccion.config(text="Ingrese la macro:")
        lAccion.pack()
        self.eTexto = ttk.Entry(self)
        self.eTexto.pack()

        self.bGuardar = ttk.Button(self, text="Guardar", command=self.guardarAccion)
        self.bGuardar.pack()

class fAccionSonido(Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.tecla  = master.tecla
        self.perfil = master.perfil
        self.accion = "sonido"

        self.crearVentana()

    def guardarAccion(self):

        accion = {
            "tecla": None,
            "comando": None,
            "parametro": None
        }
        # accion = '"tecla":"{0}","comando":"{1}","parametro":"{2}"'.format(self.tecla, self.accion, self.eTexto.get())
        accion["tecla"] = self.tecla
        accion["comando"] = self.accion
        accion["parametro"] = self.eTexto.get()

        if not teclaConComando:
            setComando(self.perfil, accion, False)
        else:
            respuesta=messagebox.askyesno("Tecla con comando", "Esta tecla ya tiene un comando asociado, desea remplazarlo?")
            if respuesta==True:
                setComando(self.perfil, accion, True)

        self.eTexto.config(textvariable="")


    def crearVentana(self):
        
        lAccion = ttk.Label(self, justify="center")
        lAccion.config(text="Seleccione el archivo de audio:")
        lAccion.pack()
        self.eTexto = ttk.Entry(self)
        self.eTexto.pack()

        self.bGuardar = ttk.Button(self, text="Guardar", command=self.guardarAccion)
        self.bGuardar.pack()

    