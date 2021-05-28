"""Sumatoria desde n hasta m """

suma = 0

numero1 = int(input("Ingrese el numero n: "))
numero2 = int(input("Ingrese el numero m: "))


for numero in range (numero1, numero2+1):
    suma = suma + numero

print(suma)



