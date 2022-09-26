from tkinter import ttk, Frame, messagebox
from vistas.ventanaInput import PreguntarNombre
from misc.perfiles import getPerfilesNombre

class FPerfiles(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master

        self.perfilActivo = None

        self.crearVentana()

    def eliminarPerfil(self, perfil):
        if perfil != '':
            r = messagebox.askquestion(title="Eliminar Perfil", message=f"Esta seguro que quiere eliminar el perfil {perfil}")
            if r == 'yes':
                print(f"perfil {perfil} eliminado")

    def nuevoPerfil(self):
        msg = PreguntarNombre(self, "Nombre de Perfil Nuevo", "Ingrese un nombre para el nuevo perfil:")
        print(msg)
        
    def crearVentana(self):
        # perfiles = ['PerfilA', 'PerfilB']
        perfiles = getPerfilesNombre()

        self.lPerf = ttk.Label(self, text="Seleccione un perfil:")
        self.lPerf.config(background="lightblue")
        self.lPerf.place(x=5, y=5)

        self.cbPerf = ttk.Combobox(self, state='readonly', values=perfiles)
        self.cbPerf.place(x=20, y=30, width=240, height=30)

        self.btnNPerf = ttk.Button(self, text='+', command=self.nuevoPerfil)
        self.btnNPerf.place(x=270, y=30, width=40, height=30)

        self.btnDPerf = ttk.Button(self, text='-', command=lambda: self.eliminarPerfil(self.cbPerf.get()))
        self.btnDPerf.place(x=310, y=30, width=40, height=30)
