import db as b
import ventanas as v
from tkinter import messagebox
def subiendo(numero, anio, mes, dia, mensaje):
   

    try:
        conexion = b.conexion
        cursor = b.cursor

        # Asegúrate de especificar la tabla y las columnas en la inserción
        cursor.execute("INSERT INTO USUARIOS (CELULAR) VALUES (?)", (numero,))
        conexion.commit()
        usuario_id = cursor.lastrowid
        cursor.execute("INSERT INTO MENSAJES (PERSONA_ID, ANIO, MES, DIA, MENSAJE) VALUES (?, ?, ?, ?, ?)", (usuario_id, anio, mes, dia, mensaje))
        conexion.commit()

        messagebox.showinfo("Exito", "Datos subidos correctamente.")
    except Exception as e:
       
        messagebox.showinfo("Error", "Error vuelva a internarlo mas tarde :(")


    
