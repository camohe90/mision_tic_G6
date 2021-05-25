numero = int(input("Ingrese un numero menor a 20 y mayor a 0: "))

while numero >= 20 or numero <= 0 :
    numero = int(input("ERROR -> Por favor ingrese un numero menor a 20 y mayor a 0: "))

print(f"El numero {numero} ingresado correctamente")