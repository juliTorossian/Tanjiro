from tkinter import ttk, Frame, Button
from misc.perfiles import teclaConComando

class FBotones(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master

        self.teclaActiva = None

        self.crearVentana()

    def click(self, tecla):
        self.teclaActiva = tecla
        # print(f"frameBotones - {tecla}")
        self.lTeclaActiva.config(text=tecla)

    def determinarColor(self, perfil, letra):
        tieneComando = teclaConComando(perfil, letra)

        return "#647E68" if tieneComando else "#D8D8D8"

    def setBotones(self, perfil):
        w = 9
        h = 4

        # self.lTeclaActiva = ttk.Label(self, text="")
        # self.lTeclaActiva.grid(row=1,column=1)
        # self.lTeclaActiva.config(background="lightblue", foreground="lightblue")

        btnA = Button(self, text='A', command=lambda: self.click('A'), width=w, height=h)
        btnA.grid(row=0,column=0,padx=10, pady=10)
        btnA.config(background=self.determinarColor(perfil, 'A'))
        btnB = Button(self, text='B', command=lambda: self.click('B'), width=w, height=h)
        btnB.grid(row=0,column=1,padx=10, pady=10)
        btnB.config(background=self.determinarColor(perfil, 'B'))
        btnC = Button(self, text='C', command=lambda: self.click('C'), width=w, height=h)
        btnC.grid(row=0,column=2,padx=10, pady=10)
        btnC.config(background=self.determinarColor(perfil, 'C'))
        btnD = Button(self, text='D', command=lambda: self.click('D'), width=w, height=h)
        btnD.grid(row=0,column=3,padx=10, pady=10)
        btnD.config(background=self.determinarColor(perfil, 'D'))
        

        btnE = Button(self, text='E', command=lambda: self.click('E'), width=w, height=h)
        btnE.grid(row=1,column=0,padx=10, pady=10)
        btnE.config(background=self.determinarColor(perfil, 'E'))
        btnF = Button(self, text='F', command=lambda: self.click('F'), width=w, height=h)
        btnF.grid(row=1,column=1,padx=10, pady=10)
        btnF.config(background=self.determinarColor(perfil, 'F'))
        btnG = Button(self, text='G', command=lambda: self.click('G'), width=w, height=h)
        btnG.grid(row=1,column=2,padx=10, pady=10)
        btnG.config(background=self.determinarColor(perfil, 'G'))
        btnH = Button(self, text='H', command=lambda: self.click('H'), width=w, height=h)
        btnH.grid(row=1,column=3,padx=10, pady=10)
        btnH.config(background=self.determinarColor(perfil, 'H'))

        btnI = Button(self, text='I', command=lambda: self.click('I'), width=w, height=h)
        btnI.grid(row=2,column=0,padx=10, pady=10)
        btnI.config(background=self.determinarColor(perfil, 'I'))
        btnJ = Button(self, text='J', command=lambda: self.click('J'), width=w, height=h)
        btnJ.grid(row=2,column=1,padx=10, pady=10)
        btnJ.config(background=self.determinarColor(perfil, 'J'))
        btnK = Button(self, text='K', command=lambda: self.click('K'), width=w, height=h)
        btnK.grid(row=2,column=2,padx=10, pady=10)
        btnK.config(background=self.determinarColor(perfil, 'K'))
        btnL = Button(self, text='L', command=lambda: self.click('L'), width=w, height=h)
        btnL.grid(row=2,column=3,padx=10, pady=10)
        btnL.config(background=self.determinarColor(perfil, 'L'))

    def crearVentana(self):
        self.lTeclaActiva = ttk.Label(self, text="")
        self.lTeclaActiva.grid(row=1,column=1)
        self.lTeclaActiva.config(background="lightblue", foreground="lightblue")
    #     w = 9
    #     h = 4

    #     self.lTeclaActiva = ttk.Label(self, text="")
    #     self.lTeclaActiva.grid(row=1,column=1)
    #     self.lTeclaActiva.config(background="lightblue", foreground="lightblue")

    #     btnA = Button(self, text='A', command=lambda: self.click('A'), width=w, height=h)
    #     btnA.grid(row=0,column=0,padx=10, pady=10)
    #     btnB = Button(self, text='B', command=lambda: self.click('B'), width=w, height=h)
    #     btnB.grid(row=0,column=1,padx=10, pady=10)
    #     btnC = Button(self, text='C', command=lambda: self.click('C'), width=w, height=h)
    #     btnC.grid(row=0,column=2,padx=10, pady=10)
    #     btnD = Button(self, text='D', command=lambda: self.click('D'), width=w, height=h)
    #     btnD.grid(row=0,column=3,padx=10, pady=10)

    #     btnE = Button(self, text='E', command=lambda: self.click('E'), width=w, height=h)
    #     btnE.grid(row=1,column=0,padx=10, pady=10)
    #     btnF = Button(self, text='F', command=lambda: self.click('F'), width=w, height=h)
    #     btnF.grid(row=1,column=1,padx=10, pady=10)
    #     btnG = Button(self, text='G', command=lambda: self.click('G'), width=w, height=h)
    #     btnG.grid(row=1,column=2,padx=10, pady=10)
    #     btnH = Button(self, text='H', command=lambda: self.click('H'), width=w, height=h)
    #     btnH.grid(row=1,column=3,padx=10, pady=10)

    #     btnI = Button(self, text='I', command=lambda: self.click('I'), width=w, height=h)
    #     btnI.grid(row=2,column=0,padx=10, pady=10)
    #     btnJ = Button(self, text='J', command=lambda: self.click('J'), width=w, height=h)
    #     btnJ.grid(row=2,column=1,padx=10, pady=10)
    #     btnK = Button(self, text='K', command=lambda: self.click('K'), width=w, height=h)
    #     btnK.grid(row=2,column=2,padx=10, pady=10)
    #     btnL = Button(self, text='L', command=lambda: self.click('L'), width=w, height=h)
    #     btnL.grid(row=2,column=3,padx=10, pady=10)
