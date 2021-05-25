suma = 0

mensaje = (
    "Ingrese los numero que desea sumar \n"
    "Ingrese el numero 0 para finalizar: "
)

numero = int(input(mensaje))

while numero != 0 :
    suma = suma + numero 
    numero = int(input(mensaje))

print("La suma de los numeros es:", suma)