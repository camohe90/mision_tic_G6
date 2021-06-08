from tkinter import *

ventana = Tk ()

boton_cerrar = Button(ventana, text = "Cerrar", command = ventana.destroy)
mensaje = Label(ventana, text="Segimos aprendiendo cosas de python")

mensaje.grid(row=0, column=0)
boton_cerrar.grid(row=0, column=1)

ventana.mainloop()