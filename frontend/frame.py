import tkinter as tk
from tkinter import ttk,messagebox
from PIL import ImageTk, Image

from Analizador.gramatica import analizar_entrada
from Interprete.Controlador import Controlador
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos





class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Compilador")
        self.ventana.geometry("1200x500")
        #self.ventana.rowconfigure(0,minsize=300,weight=0)
        #self.ventana.columnconfigure(1,minsize=600,weight=1)
        self.createWidgets()
        self.ventana.mainloop()

    def createWidgets(self):
        #CUADROS DE TEXTO
        self.text_editor = tk.Text(self.ventana,width=62, height=20)
        self.text_console = tk.Text(self.ventana,width=62, height=20)

        self.text_console.place(x=640,y=50)
        self.text_editor.place(x=60,y=50)



        #BOTONES
        frameBotones = tk.Frame(self.ventana)
        frameBotones.pack(fill="x", side="top")

        botonCompilar = tk.Button(frameBotones,text="Compilar",command=lambda:(self.compilar()))
        botonEditor = tk.Button(frameBotones,text="Editor")
        botonReportes = tk.Button(frameBotones, text="Reportes")
        botonAcerca = tk.Button(frameBotones,text="Acerca de")

        botonEditor.pack(side="left")
        botonCompilar.pack(side="left")
        botonReportes.pack(side="left")
        botonAcerca.pack(side="left")

    def compilar(self):
        self.text_console.delete("1.0",tk.END)
        input = self.text_editor.get(0.1, tk.END)
        nodos = analizar_entrada(input)
        controlador = Controlador()
        ts = TablaSimbolos(None)
        for nodo in nodos:
            print("---------------------------------------------------")
            print(nodo)
            nodo.ejecutar(controlador, ts)
            # print(nodo)
            # print(nodo.getTipo(controlador,ts))
            # print(nodo.getValor(controlador,ts))
        self.text_console.insert("0.1",controlador.consola)
        print(controlador.consola)


