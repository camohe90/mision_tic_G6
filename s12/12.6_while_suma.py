from typing import NoReturn


suma = 0

mensaje = ("Ingrese los numero que desea sumar: ")

while(suma <= 100):
    numero = int(input(mensaje))
    suma = suma + numero

print("La suma de los numeros es:", suma)