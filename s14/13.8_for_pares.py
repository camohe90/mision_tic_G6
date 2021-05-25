numeros_guardados = []
suma = 0

numeros_almacenar= int(input("Digite la cantidad de numeros que desea almacenar: "))

# Valido que el usuario inrese un numero mayor que 0
while numeros_almacenar <= 0:
    print("Por favor ingrese un numero positivo")
    numeros_almacenar= int(input("Digite la cantidad de numeros que desea almacenar: "))

# Guardo en la lista numeros_guardados la informacion ingresada por el usuario
for contador in range(numeros_almacenar):
    numeros_guardados.append(int(input(f"Digite el numero {contador +1} que desea almacenar: ")))

print(numeros_guardados)

# Recorro la lista numeros_guardados y reviso cuales numero son pares
for numero in numeros_guardados:
    if numero % 2 == 0:
        suma = suma + numero

print(f"La suma de los numeros pares es {suma}")
