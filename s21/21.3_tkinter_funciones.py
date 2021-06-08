from tkinter import *

def mostrar_mensaje():
    mensaje.configure(text="Estamos volando al crea interfaces de usuario")


ventana = Tk ()

mensaje = Label(ventana,fg="BlueViolet", bg="white", font=("Tahoma", 14))
boton_mensaje = Button(ventana, text="mostrar", command=mostrar_mensaje)
boton_cerrar = Button(ventana, text = "cerrar", command = ventana.destroy)

mensaje.grid(row=0, column=0)
boton_mensaje.grid(row=1, column=0)
boton_cerrar.grid(row=1, column=1)


ventana.mainloop()