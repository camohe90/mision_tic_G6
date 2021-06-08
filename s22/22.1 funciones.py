from tkinter import *


# bloque de funciones
def mostrar_mensaje():
    mensaje.configure(text="Estamos volando con python ")


# Defino mi variable ventana como el elemento principal de tkinter.
ventana = Tk()

# Definir que elementos tiene mi interfaz grafica
mensaje = Label(ventana, fg="red", bg="white", font=("Arial",))
boton_mostar = Button(ventana, text="Mostrar", command=mostrar_mensaje)
boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)

# Ubicar los elementos en la pantalla
mensaje.grid(row=0, column=0, columnspan=2)
boton_mostar.grid(row=1, column=0)
boton_cerrar.grid(row=1, column=1)

# Sin esto no funciona
ventana.mainloop()