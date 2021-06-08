from tkinter import *

ventana = Tk ()

boton_cerrar = Button(ventana, text = "Cerrar", command = ventana.destroy)
boton_cerrar.grid()

ventana.mainloop()