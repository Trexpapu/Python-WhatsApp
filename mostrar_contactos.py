import db as b 
import ventanas as v 
import borrar_modificar_contacto as bmc

def formulario():
    def obtenerDatosSeleccionados(event):
        # Obtenemos el índice de la fila seleccionada
        item = tabla.selection()[0]
        
        # Obtenemos los valores de todas las columnas de esa fila
        valores = tabla.item(item, 'values')
        
        # Los valores de la fila están en la variable 'valores'
        id = valores[0]
        nombre = valores[1]
        celular = valores[2]
        
        bmc.borrarOeliminar(id,nombre,celular)

    try:
        # Llamar conexión y realizar consulta
        conexion = b.conexion
        cursor = b.cursor
        cursor.execute("SELECT C.ID, C.NOMBRE, C.CELULAR FROM CONTACTOS AS C")
        datos_combinados = cursor.fetchall()
    except Exception as e:
        # Manejo de excepciones en caso de error
        datos_combinados = None

    # Crear ventana
    ventana_mostrar = v.MiVentana("Usuarios, doble click para seleccionar", "#2CCDA1")

    # Verificar si hubo un error en la consulta
    if datos_combinados is None:
        fuente_personalizada = ("Arial", 14)
        mensaje_error = v.tk.Label(ventana_mostrar, text="Error al obtener los datos de la base de datos", font=fuente_personalizada, width=40, height=3, bg="red", relief="sunken", borderwidth=2)
        mensaje_error.pack(padx=20, pady=20)
    else:
        # Crear un frame que contendrá el Treeview y las barras de desplazamiento
        frame = v.ttk.Frame(ventana_mostrar)
        frame.pack(fill="both", expand=True)
        
        # Crear barras de desplazamiento
        yscroll = v.ttk.Scrollbar(frame, orient="vertical")
        xscroll = v.ttk.Scrollbar(frame, orient="horizontal")
        
        # Crear un widget Treeview para mostrar los datos
        tabla = v.ttk.Treeview(frame, columns=("ID", "NOMBRE", "CELULAR"),
                        yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        yscroll.config(command=tabla.yview)
        xscroll.config(command=tabla.xview)

        tabla.heading("#1", text="ID")
        tabla.heading("#2", text="NOMBRE")
        tabla.heading("#3", text="CELULAR")
        
        
        # Llenar la tabla con los datos
        for dato in datos_combinados:
            tabla.insert("", "end", values=dato)
        
        # Configurar el evento de doble clic en la tabla
        tabla.bind("<Double-1>", obtenerDatosSeleccionados)
    
        # Empacar los widgets en el frame
        yscroll.pack(side="right", fill="y")
        xscroll.pack(side="bottom", fill="x")
        tabla.pack(fill="both", expand=True)
    
    ventana_mostrar.mainloop()
    

