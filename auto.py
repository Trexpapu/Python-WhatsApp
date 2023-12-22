import db as d
import webbrowser, pyautogui
import time as t
import pygame as p
from tkinter import messagebox
conexion = d.conexion
cursor = d.cursor
def eliminarUsuariosSinMensaje():
    try:
       # print("xd")
        # Ejecuta la sentencia SQL para eliminar usuarios sin mensajes
        cursor.execute("DELETE FROM USUARIOS WHERE ID NOT IN (SELECT DISTINCT PERSONA_ID FROM MENSAJES)")
        
        # Confirma los cambios y cierra la conexión
        conexion.commit()

        #eliminar antiguos registros


    except Exception:

        messagebox.showinfo("Error", "Hay datos que no se pudieron borrar")



def enviar_mensajes():
    p.init()
    p.mixer.init()
    sound = p.mixer.Sound('sonido.mp3')

    estructura_tiempo = t.localtime(t.time())
    try:
        cursor.execute("SELECT * FROM USUARIOS")
        usuarios = cursor.fetchall()
        cursor.execute("SELECT * FROM MENSAJES")
        mensajes = cursor.fetchall()
        fecha_actual = f"{estructura_tiempo.tm_year} {estructura_tiempo.tm_mon} {estructura_tiempo.tm_mday}"
        indice = 0
        mensajes_encontrados = False
        webbrowser.open("https://web.whatsapp.com")
        t.sleep(60)

        for mensaje in mensajes:
            fecha = f"{mensaje[2]} {mensaje[3]} {mensaje[4]}"
            
            if fecha_actual == fecha:
                #igual
                celular_destino =f"{usuarios[indice][1]}"
                print(celular_destino, mensaje[5], mensaje[0])
                webbrowser.open("https://web.whatsapp.com/send?phone="+f"{celular_destino}")
                t.sleep(30)
                pyautogui.typewrite(mensaje[5])
                t.sleep(3)
                pyautogui.press("enter")
                t.sleep(10)
                id_ = mensaje[0]
                cursor.execute("DELETE FROM MENSAJES WHERE ID = ?", (id_,))
                conexion.commit()
                mensajes_encontrados = True
            indice += 1        
            
        sound.play()
        p.time.wait(int(sound.get_length() * 1000))
        p.quit()
       



    except Exception as e:
        messagebox.showinfo("Error", "Ocurrio un error al enviar los mensajes")
    finally:

        if mensajes_encontrados == False:
            messagebox.showinfo("Error", "No hay mensajes por enviar hoy")
        elif mensajes_encontrados == True:
            messagebox.showinfo("Exito","Mensajes enviados")
    



