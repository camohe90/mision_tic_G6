"""Sumatoria desde n hasta m """

suma = 0

numero1 = int(input("Ingrese el numero n: "))
numero2 = int(input("Ingrese el numero m: "))

if numero1 > numero2 :
    print(f"El numero1: {numero1} es mayor que el numero2:{numero2}, no puedo hacer la sumatoria")
else:
    for numero in range (numero1, numero2+1):
        suma = suma + numero
    print(suma)



