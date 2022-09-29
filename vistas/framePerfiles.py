from tkinter import ttk, Frame, messagebox
from vistas.ventanaInput import PreguntarNombre
from misc.perfiles import delPerfil, getPerfilesNombre, setPerfil

class FPerfiles(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master

        self.puertoCOM = None
        self.perfilActivo = None

        self.crearVentana()

    def setPerfilSel(self, perfil):
        perfiles = getPerfilesNombre()
        self.cbPerf.config(values=perfiles)
        # self.cbPerf.current(f"[{perfil}]")
        self.cbPerf.set("")
        self.cbPerf.set(perfil)

    def eliminarPerfil(self, perfil):
        if perfil != '':
            r = messagebox.askquestion(title="Eliminar Perfil", message=f"Esta seguro que quiere eliminar el perfil {perfil}")
            if r == 'yes':
                print(f"perfil {perfil} eliminado")
                ok = delPerfil(perfil)
                if ok:
                    messagebox.showinfo("Perfil eliminado", f"El perfil {perfil} fue eliminado satisfactoriamente.")
                    self.setPerfilSel("")
                else:
                    messagebox.showerror("Error", "Ha ocurrido un erro al eliminar el perfil.")

    def activarPerfil():
        pass

    def nuevoPerfil(self):
        cantPerfiles = len(getPerfilesNombre())
        perfilNombre = self.cbPerf.get()
        if len(perfilNombre) > 0:
            if cantPerfiles > 0 and cantPerfiles < 12:
                r = messagebox.askquestion(title="Nuevo Perfil", message=f"Desea crear un nuevo perfil llamado: {perfilNombre}?")
                if r == 'yes':
                    print(f"perfil {perfilNombre} creado")
                    ok = setPerfil(perfilNombre)
                    self.setPerfilSel(perfilNombre)

                    if not ok:
                        messagebox.showwarning("Ya existe perfil", f"Ya existe un perfil con ese nombre ({perfilNombre}).")
            else:
                messagebox.showerror("Error", "Has alcanzado la cantidad maxima de perfiles (12).")
        
    def crearVentana(self):
        perfiles = getPerfilesNombre()

        self.lPerf = ttk.Label(self, text="Seleccione un perfil:")
        self.lPerf.config(background="lightblue")
        self.lPerf.place(x=5, y=5)

        self.cbPerf = ttk.Combobox(self, values=perfiles)
        self.cbPerf.place(x=20, y=30, width=240, height=30)

        self.btnNPerf = ttk.Button(self, text='+', command=self.nuevoPerfil)
        self.btnNPerf.place(x=270, y=30, width=40, height=30)

        self.btnDPerf = ttk.Button(self, text='-', command=lambda: self.eliminarPerfil(self.cbPerf.get()))
        self.btnDPerf.place(x=310, y=30, width=40, height=30)

        self.bActivarPerfil = ttk.Button(self, text='Activar')
        self.bActivarPerfil.place(x=150, y=65, width=80, height=30)
