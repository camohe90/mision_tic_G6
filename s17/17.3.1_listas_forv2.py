"""Programa que me permita ingresar 10 numeros
    me imprima el promedio de los numeros ingresados
    me imprima el mayor y el menor
    que me genere una lista con los pares y otra con los impares"""

total = 0
numeros_ingresados = []
pares = []
impares = []

for numero in range (10):
    mensaje = f"Ingrese el numero {numero +1}: "
    numeros_ingresados.append( int(input(mensaje))) # Agrego el numero ingresado a la lista de numeros

for numero in numeros_ingresados:
    total += numero
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print(f"El promedio de los numeros ingresados es: {total / len(numeros_ingresados)}")
print(f"El numero menor en la ista de numeros ingresados es: {min(numeros_ingresados)}")
print(f"El numero mayor en la lista de numeros ingresados es: {max(numeros_ingresados)}")
print(f"Los numeros pares que hay en los numeros ingresados son {pares}")
print(f"Los numeros impares que hay en los numeros ingresados son {impares}")
