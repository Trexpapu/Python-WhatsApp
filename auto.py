import db as d
import webbrowser, pyautogui
import time as t
import pygame as p
from tkinter import messagebox
import speedtest 
conexion = d.conexion
cursor = d.cursor
def eliminarUsuariosSinMensaje():
    try:

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

    st = speedtest.Speedtest()
    vel_descarga = st.download() / 10**6  # Convertir a megabits por segundo
    tiempo = 60
    if vel_descarga <=10:
        tiempo = 90
    elif vel_descarga <=20:
        tiempo = 50
    elif vel_descarga <= 50:
        tiempo = 28
    elif vel_descarga <= 100:
        tiempo = 22
    else:
        tiempo = 15
   # print(f"Velocidad de descarga: {vel_descarga:.2f} Mbps")
   # print(tiempo)

    try:
        cursor.execute("SELECT * FROM MENSAJES")
        mensajes = cursor.fetchall()
        fecha_actual = f"{estructura_tiempo.tm_year} {estructura_tiempo.tm_mon} {estructura_tiempo.tm_mday}"
        mensajes_encontrados = False
        webbrowser.open("https://web.whatsapp.com")
        t.sleep(tiempo)

        for mensaje in mensajes:
            fecha = f"{mensaje[2]} {mensaje[3]} {mensaje[4]}"
            
            if fecha_actual == fecha:
                #igual
                cursor.execute("SELECT U.CELULAR FROM USUARIOS AS U WHERE ID = ?", (mensaje[1], ))
                celular_destino = cursor.fetchone()
                #celular_destino =f"{usuarios[indice][1]}"
             #   print(celular_destino, mensaje[5], mensaje[0])
                webbrowser.open("https://web.whatsapp.com/send?phone="+f"{celular_destino}")
                t.sleep(tiempo)
                pyautogui.typewrite(mensaje[5])
                t.sleep(5)
                pyautogui.press("enter")
                t.sleep(15)
                id_ = mensaje[0]
                cursor.execute("DELETE FROM MENSAJES WHERE ID = ?", (id_,))
                conexion.commit()
                mensajes_encontrados = True

        sound.play()
        p.time.wait(int(sound.get_length() * 1000))
        p.quit()
       



    except Exception as e:
        print(e)
        messagebox.showinfo("Error", "Ocurrio un error al enviar los mensajes")
    finally:

        if mensajes_encontrados == False:
            messagebox.showinfo("Error", "No hay mensajes por enviar hoy")
        elif mensajes_encontrados == True:
            messagebox.showinfo("Exito","Mensajes enviados")
