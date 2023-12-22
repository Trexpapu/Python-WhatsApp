import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
class MiVentana(tk.Tk):#clase ventana
    def __init__(self, titulo, color):#funcion inicial que recibe parametros titulo y color de ventana
        super().__init__()#heredamos las funciones de tkinter
        self.title(titulo)#agregamos titulo
        self.state('zoomed')  # Maximiza la ventana
        self.configure(bg=color)  # Puedes usar cualquier color válido
        
    def generarLabel(self, texto, fuente, ancho, altura, color, relieve, borde, posx, posy):
        self.label = tk.Label(text=texto, font=fuente, width=ancho, height=altura, bg=color, relief=relieve, bd=borde)
        self.label.place(x=posx, y=posy)

    def generarEntry(self,fuente, color, colorTexto, justificacion, colorCursor, relieve, posx, posy, ancho, altura, variable):
        self.entry = tk.Entry(self, font = fuente, bg=color, fg=colorTexto, justify=justificacion, insertbackground=colorCursor, relief=relieve, textvariable=variable)
        self.entry.place(x=posx,y=posy,width=ancho,height=altura)