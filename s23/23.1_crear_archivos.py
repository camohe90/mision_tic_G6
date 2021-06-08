archivo = open("txt/reporte.txt","w")
archivo.write("Hola clase\n")
archivo.write("Se esta acabando el curso :( :(" )
archivo.close()

with open ("txt/reporte.txt","w") as archivo:
    archivo.write("Hola clase\n")
    archivo.write("Se esta acabando el curso :( :(\n" )
    archivo.write("Les queda un maravilloso camino por recorrer \n")
    archivo.write("El jueves espero que todos prendan sus camaras para la despedida")

