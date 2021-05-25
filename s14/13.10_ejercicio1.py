"""Escribir un programa que permita al usuario ingresar 6 números enteros,
que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria
de los números negativos y el promedio de los positivos"""
numeros_ingresados = []
sumatoria = 0
promedio = 0
contador = 0

for contar in range (6):
    numero = int(input("Ingrese un numero"))
    numeros_ingresados.append(numero)

print(numeros_ingresados)

for numero in numeros_ingresados:
    if(numero < 0):
        sumatoria = sumatoria + numero
    else:
        promedio = promedio + numero
        contador +=1

if contador > 0:
    print("El promedio de los numeros es", round(promedio/contador,2))
else:
    print("No se ingresadon numero positivos no se puede calcular el promedio")

print("La sumatoria es", sumatoria)