import tkinter as tk
from tkinter import ttk, Frame

class PreguntarNombre(Frame):

    def __init__(self, master, titulo, mensaje) -> None:
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        # self.ventana.geometry('300x200')
        self.ventana.resizable(False,False)
        window_width = 300
        window_height = 200
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.ventana.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.value = None
        self.mensaje = mensaje

        self.crearVentana()

    def btnOk(self, input):
        if input != '':
            # print(input)
            self.value = input
            # self.ventana.destroy()
    def btnCancel(self):
        self.ventana.destroy()


    def crearVentana(self):
        self.lText = ttk.Label(self.ventana, text=self.mensaje)
        self.lText.pack()

        self.entry = ttk.Entry(self.ventana)
        self.entry.pack()
        self.entry.focus()

        self.btnOk = ttk.Button(self.ventana, text='Guardar') # , command=lambda: self.btnOk(self.entry.get())
        self.btnOk.pack()
        self.btnCan = ttk.Button(self.ventana, text='Cancelar', command=lambda: self.btnCancel())
        self.btnCan.pack()