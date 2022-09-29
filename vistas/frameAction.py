from tkinter import ttk, Frame, messagebox, filedialog
from tktooltip import ToolTip
from misc.perfiles import setComando, teclaConComando
from os import path
from funciones.teclas.teclado import grabarMacro

acciones = ["Macro", "Escritura", "Sonido"]

class FActions(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.perfil      = None
        self.tecla       = None
        self.fAccion     = None
        self.accionSelec = None
        self.accParam    = ''

        self.crearVentana()

    def getTecla(self):
        return self.tecla
    def getPerfil(self):
        return self.perfil

    def setPerfil(self, perfil):
        self.perfil = perfil
        self.lPerfil.config(text="Perfil: {}".format(self.perfil), justify='right')
    def setBtn(self, tecla):
        self.tecla = tecla
        self.lTecla.config(text="Tecla: {}".format(self.tecla))
    def setAccParam(self, param):
        self.accParam = param
        print(self.accParam)

    def setAccion(self, accion):
        print(accion)

        if (self.tecla != None and self.perfil != None):
            if (accion != None):
                if (accion.lower() != self.accionSelec):
                    if (self.fAccion != None):
                        self.fAccion.destroy()
                    
                    if (accion.lower() == "escritura"):
                        self.fAccion = fAccionEscritura(self, self.accParam)
                        # self.fAccion.pack()
                        self.fAccion.place(x=30, y=110, width=320, height=190)
                        self.accionSelec = accion.lower()
                    elif (accion.lower() == "macro"):
                        self.fAccion = fAccionMacro(self, self.accParam)
                        # self.fAccion.pack()
                        self.fAccion.place(x=30, y=110, width=320, height=190)
                        self.accionSelec = accion.lower()
                    elif (accion.lower() == "sonido"):
                        self.fAccion = fAccionSonido(self, self.accParam)
                        # self.fAccion.pack()
                        self.fAccion.place(x=30, y=110, width=320, height=190)
                        self.accionSelec = accion.lower()


    def crearVentana(self):
        self.lPerfil = ttk.Label(self, text="Perfil: {}".format(self.perfil))
        # self.lPerfil.pack()
        self.lPerfil.place(x=50,y=20,width=140)
        self.lTecla = ttk.Label(self, text="Tecla: {}".format(self.tecla))
        # self.lTecla.pack()
        self.lTecla.place(x=160,y=20,width=140)

        self.cbAcciones = ttk.Combobox(self, state='readonly', values=acciones)
        # self.cbAcciones.pack()
        self.cbAcciones.place(x=120, y=60, width=140, height=30)
        # self.cbAcciones.bind("<<ComboboxSelected>>", self.cambioDeAccion())
        
class fAccionEscritura(Frame):
    
    def __init__(self, master, param):
        super().__init__(master)
        self.master = master
        self.tecla  = master.tecla
        self.perfil = master.perfil
        self.accion = "escribir"
        self.param  = param

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

        if not teclaConComando(self.perfil, self.tecla):
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
        self.eTexto = ttk.Entry(self, textvariable=self.param)
        self.eTexto.pack()

        self.bGuardar = ttk.Button(self, text="Guardar", command=self.guardarAccion)
        self.bGuardar.pack()

class fAccionMacro(Frame):
    
    def __init__(self, master, param):
        super().__init__(master)
        self.master = master
        self.tecla  = master.tecla
        self.perfil = master.perfil
        self.accion = "macro"
        self.macro  = None
        self.param  = param

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
        accion["parametro"] = self.eTexto['text']

        if not teclaConComando(self.perfil, self.tecla):
            setComando(self.perfil, accion, False)
        else:
            respuesta=messagebox.askyesno("Tecla con comando", "Esta tecla ya tiene un comando asociado, desea remplazarlo?")
            if respuesta==True:
                setComando(self.perfil, accion, True)

        self.eTexto.config(text="")

    def grabarMacro(self):
        
        self.macro = grabarMacro()

        self.eTexto.config(text=self.macro)

    def crearVentana(self):
        
        lAccion = ttk.Label(self, justify="center")
        lAccion.config(text="Ingrese la macro:")
        lAccion.pack()
        self.eTexto = ttk.Label(self, justify="center", text=self.param)
        self.eTexto.pack()
        self.bGuardar = ttk.Button(self, text="Grabar Macro", command=self.grabarMacro)
        self.bGuardar.pack()

        self.bGuardar = ttk.Button(self, text="Guardar", command=self.guardarAccion)
        self.bGuardar.pack()

class fAccionSonido(Frame):
    
    def __init__(self, master, param):
        super().__init__(master)
        self.master = master
        self.tecla  = master.tecla
        self.perfil = master.perfil
        self.accion = "sonido"
        self.archivo = None
        self.param  = param

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
        accion["parametro"] = self.archivo

        if not teclaConComando(self.perfil, self.tecla):
            setComando(self.perfil, accion, False)
        else:
            respuesta=messagebox.askyesno("Tecla con comando", "Esta tecla ya tiene un comando asociado, desea remplazarlo?")
            if respuesta==True:
                setComando(self.perfil, accion, True)

        self.eTexto.config(textvariable="")

    def buscarArchivo(self):
        filetypes = [("MP3", "*.mp3")]
        self.archivo = filedialog.askopenfilename(initialdir='/', title='Seleccione un archivo de audio',filetypes = filetypes)
        nomArchivo = path.split(self.archivo)
        print(self.archivo)
        print(nomArchivo[1])
        self.eTexto.config(text=nomArchivo[1])
        tooltip = self.archivo
        ToolTip(self.eTexto, msg=tooltip, delay=1.0)


    def crearVentana(self):
        
        lAccion = ttk.Label(self, justify="center")
        lAccion.config(text="Seleccione el archivo de audio:")
        lAccion.pack()
        self.eTexto = ttk.Label(self, justify="center", text=self.param)
        self.eTexto.pack()
        bSelArch = ttk.Button(self, text="Buscar Archivo", command=self.buscarArchivo)
        bSelArch.pack()

        self.bGuardar = ttk.Button(self, text="Guardar", command=self.guardarAccion)
        self.bGuardar.pack()

    