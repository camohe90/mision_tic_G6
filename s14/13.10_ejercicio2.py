"""Escribir un programa que permita al usuario ingresar dos años y
luego imprima todos los años en ese rango, que sean bisiestos y
múltiplos de 10"""


anio1 = int(input("Ingrese el primer año que desea validar"))
anio2 = int(input("Ingrese el segundo año que desea validar"))

for anio in range(anio1,anio2):
    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) and anio % 10 == 0:
        print(f"{anio} es bisiesto")

