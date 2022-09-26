from tkinter import ttk, Frame
from misc.obtenerPuertosCOM import puertos_seriales


class FConn(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.crearVentana()

    def conn(self):
        puerto = self.cbCOM.get()
        if puerto != '':
            print("conectado al puerto {}".format(puerto))
            self.lConn.config(text="CONECCION OK")
            self.lConn.config(justify="center")
            self.lConn.config(background="#03AC13")
    
    def crearVentana(self):
        puertosCOM = puertos_seriales()
        self.cbCOM = ttk.Combobox(self, state='readonly', values=puertosCOM)
        self.cbCOM.place(x=15, y=15, width=180, height=30)
        self.btnConn = ttk.Button(self, text="CONN", command=self.conn)
        self.btnConn.place(x=200, y=15, width=50, height=30)
        self.lConn = ttk.Label(self, text="")
        self.lConn.place(x=540, y=15, width=230, height=30)

    
    