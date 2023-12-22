import db as b
import ventanas as v
from tkinter import messagebox
import time as t
import pygame as p
def regresar(ventana):
    ventana.destroy()

def esperar5seg():
    t.sleep(1)
    v_formulario.destroy()

def formulario():
    p.init()
    def enviar(nombre, numero):
     
        if nombre and numero:   
            try:
                conexion = b.conexion
                cursor = b.cursor

                # Asegúrate de especificar la tabla y las columnas en la inserción
                cursor.execute("INSERT INTO CONTACTOS (NOMBRE, CELULAR) VALUES (?, ?)", (nombre,numero))
                conexion.commit()
                messagebox.showinfo("Exito", "Datos subidos correctamente.")
            except Exception as e:
               
                messagebox.showinfo("Error", "Error vuelva a internarlo mas tarde :(") 
        else:
            messagebox.showinfo("Error", "Faltan campos por llenar")
            esperar5seg()

    global v_formulario
    info = p.display.Info()
    ancho = info.current_w
    alto = info.current_h
    v_formulario = v.MiVentana("Agregar contacto", "#102356")
    fuente_personalizada = ("Times New Roman", 12)#fuente y tamaño de la letra para botones
    #label Nombre

    label_Nombre = v.tk.Label(v_formulario, text=f"Nombre: ", font=fuente_personalizada, width=14, height=3, bg="#009aff", relief="sunken", bd=2)
    label_Nombre.place(x=ancho-ancho + 400, y=alto-alto+50)
    #entry Nombre
    entry_Nombre = v.tk.Entry(v_formulario, font=fuente_personalizada, bg ="white", fg = "black", justify="left", insertbackground="green", relief="sunken")
    entry_Nombre.place(x = ancho-ancho + 600, y=alto-alto+60, width=250, height=55)


    #label año 
    label_Celular = v.tk.Label(v_formulario, text=f"Celular: ", font=fuente_personalizada, width=10, height=3, bg="#009aff", relief="sunken", bd=2)
    label_Celular.place(x=ancho-ancho + 400, y=alto-alto+150)
    #entry año

    entry_Celular = v.tk.Entry(v_formulario, font=fuente_personalizada, bg ="white", fg = "black", justify="left", insertbackground="green", relief="sunken")
    entry_Celular.place(x = ancho-ancho + 600, y=alto-alto+155, width=150, height=55)

    v_formulario.boton_regresar = v.tk.Button(v_formulario, text="Regresar al menu", command=lambda: regresar(v_formulario), font = fuente_personalizada, width=20, height=5, bg = "#BBD631")
    v_formulario.boton_regresar.place(x=ancho-ancho + 40, y=alto-alto+20)


    #enviar datos
    v_formulario.boton_enviar = v.tk.Button(v_formulario, text="Subir datos", command=lambda : enviar(entry_Nombre.get(), entry_Celular.get()), font = fuente_personalizada, width=20, height=5, bg = "#0a8012")
    v_formulario.boton_enviar.place(x=ancho-200, y=alto-alto+20)
    v_formulario.mainloop()

