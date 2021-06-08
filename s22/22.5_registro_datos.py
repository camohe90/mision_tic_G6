from tkinter import *

clientes = []

def borrar_datos():
    info_nombre.set("")
    info_apellido.set("")
    info_cedula.set("")
    mensaje["text"] = ""

def guardar_clientes():
    nombre1 = info_nombre.get()
    apellido1 = info_apellido.get()
    cedula1 = info_cedula.get()
    clientes.append(nombre1 + " " + apellido1+ "  "+ cedula1 )
    mensaje["text"] = "Cliente guardado"
    ventana.after(2000, borrar_datos)

def mostrar_clientes():
    pass

ventana = Tk()
ventana.geometry("800x600")


info_nombre = StringVar()
info_apellido = StringVar()
info_cedula = StringVar()


nombre = Label(ventana, text="Nombre: ")
apellido = Label(ventana, text="Apellido: ")
cedula = Label(ventana, text="Cédula: ")
mensaje = Label(ventana, fg="red", font=("Arial",12))

entrada_nombre = Entry(ventana, width=25, justify=LEFT, textvariable= info_nombre)
entrada_apellido = Entry(ventana, width=25, justify=LEFT, textvariable= info_apellido)
entrada_cedula = Entry(ventana, width=25, justify=LEFT, textvariable= info_cedula)

boton_guardar = Button(ventana, text="Guardar", command=guardar_clientes)
boton_mostrar = Button(ventana, text="Mostrar", command=mostrar_clientes)

nombre.grid(row=0, column=0)
entrada_nombre.grid(row=0, column=1)

apellido.grid(row=1, column=0)
entrada_apellido.grid(row=1, column=1)

cedula.grid(row=2, column=0)
entrada_cedula.grid(row=2, column=1)

boton_guardar.grid(row=3,column=0)
boton_mostrar.grid(row=3, column=1)

mensaje.grid(row=4, column=0, columnspan=2)


ventana.mainloop()