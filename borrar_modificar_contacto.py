import ventanas as v
import db as b
import time as t
from tkinter import messagebox
import threading 
import pygame as p 
p.init()
info = p.display.Info()
ancho = info.current_w
alto = info.current_h
def regresar(ventana):
    ventana.destroy()

def esperar5seg():
    t.sleep(1)
    ventana_formulario.destroy()
def eliminarRegistro(id_a_eliminar):
    
    try:
        # Establece la conexión a la base de datos
        conexion = b.conexion
        cursor = b.cursor

        # Ejecuta la sentencia SQL para eliminar el registro por su ID
        cursor.execute("DELETE FROM CONTACTOS WHERE ID = ?", (id_a_eliminar,))
        # Confirma los cambios y cierra la conexión
        conexion.commit()
        
        messagebox.showinfo("Exito", "Datos borrados correctamente")
        hilo1 = threading.Thread(target=esperar5seg)
        hilo1.start()
    except Exception:
        messagebox.showinfo("Error", "No se pudieron borrar los registros")
        hilo1 = threading.Thread(target=esperar5seg)
        hilo1.start()

    


def modificarRegistro(id_, nombre_, celular_):
    
    try:
        # Establece la conexión a la base de datos
        conexion = b.conexion
        cursor = b.cursor

        cursor.execute("UPDATE CONTACTOS SET NOMBRE = ?, CELULAR = ? WHERE ID = ?", (nombre_, celular_, id_))
        # Confirma los cambios y cierra la conexión
        conexion.commit()
        
        messagebox.showinfo("Exito", "Datos modificados correctamente.")
        hilo1 = threading.Thread(target=esperar5seg)
        hilo1.start()
    except Exception:
        messagebox.showinfo("Error", "No se pudieron modificar los registros ")
        hilo1 = threading.Thread(target=esperar5seg)
        hilo1.start()
        
   
    

def borrarOeliminar(id, nombre, celular):
    # Crear ventana
    global ventana_formulario
    ventana_formulario = v.MiVentana("Modificar o Eliminar", "#102356")
    fuente_personalizada = ("Times New Roman", 12)#fuente y tamaño de la letra para botones
    #label celular
    label_nombre = v.tk.Label(ventana_formulario, text=f"Nombre: ", font=fuente_personalizada, width=14, height=3, bg="#009aff", relief="sunken", bd=2)
    label_nombre.place(x=ancho-ancho+500, y=alto-alto+50)
    #entry celular

    entry_nombre = v.tk.Entry(ventana_formulario, font=fuente_personalizada, bg ="white", fg = "black", justify="left", insertbackground="green", relief="sunken")
    entry_nombre.place(x = ancho-ancho +700, y=alto-alto+60, width=180, height=55)
    entry_nombre.insert(0, nombre)

    #label año 
    label_celular = v.tk.Label(ventana_formulario, text=f"Celular: ", font=fuente_personalizada, width=10, height=3, bg="#009aff", relief="sunken", bd=2)
    label_celular.place(x=ancho-ancho+500, y=alto-alto+150)
    #entry año
    
    entry_celular = v.tk.Entry(ventana_formulario, font=fuente_personalizada, bg ="white", fg = "black", justify="left", insertbackground="green", relief="sunken")
    entry_celular.place(x = ancho-ancho+700, y=alto-alto+155, width=180, height=55)
    entry_celular.insert(0, celular)
   
    
    
    # Crear botones para eliminar y modificar
    boton_eliminar = v.tk.Button(ventana_formulario, text="Eliminar", command=lambda:eliminarRegistro(id), width=8, height=4, bg="#C62828", font = fuente_personalizada)
    boton_modificar = v.tk.Button(ventana_formulario, text="Modificar", command=lambda: modificarRegistro(id, entry_nombre.get(), entry_celular.get()), width=8, height=4, bg="#66BB6A", font=fuente_personalizada)    
    boton_regresar = v.tk.Button(ventana_formulario, text="Regresar", command=lambda: regresar(ventana_formulario), font = fuente_personalizada, width=15, height=4, bg = "#BBD631")
    boton_eliminar.place(x=ancho-800, y=alto-alto+600)
    boton_modificar.place(x=ancho-1000, y=alto-alto+600)
    boton_regresar.place(x=ancho-ancho+25, y=alto-alto+25)
    
    ventana_formulario.mainloop()