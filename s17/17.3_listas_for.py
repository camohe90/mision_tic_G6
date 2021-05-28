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
    numero_ingesado = int(input(mensaje))  # Solicito un numero al usuario
    numeros_ingresados.append(numero_ingesado) # Agrego el numero ingresado a la lista de numeros

for numero in numeros_ingresados:
    total += numero
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

promedio = total / len(numeros_ingresados)
menor = min(numeros_ingresados)
mayor = max(numeros_ingresados)

print(f"El promedio de los numeros ingresados es: {promedio}")
print(f"El numero menor en la ista de numeros ingresados es: {menor}")
print(f"El numero mayor en la lista de numeros ingresados es: {mayor}")
print(f"Los numeros pares que hay en los numeros ingresados son {pares}")
print(f"Los numeros impares que hay en los numeros ingresados son {impares}")
