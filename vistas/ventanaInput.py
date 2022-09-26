import tkinter as tk
from tkinter import ttk

class PreguntarNombre(ttk.Frame):

    def __init__(self, master, titulo, mensaje) -> None:
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        self.ventana.geometry('300x200')

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
        lText = ttk.Label(self.ventana, text=self.mensaje)
        lText.pack()

        entry = ttk.Entry(self.ventana)
        entry.pack()
        entry.focus()

        btnOk = ttk.Button(self.ventana, text='Guardar', command=lambda: self.btnOk(entry.get()))
        btnOk.pack()
        btnCan = ttk.Button(self.ventana, text='Cancelar', command=lambda: self.btnCancel())
        btnCan.pack()