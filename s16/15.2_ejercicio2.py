"""Implementar un programa que se muestren todos los multiplos de 6 entre 6 y 150 
    ambos inclusive"""

numero1 = int(input("Ingrese el numero n: "))
numero2 = int(input("Ingrese el numero m: "))

multiplos = []

for numero in range (numero1,(numero1*numero2 )+1):
    if(numero % numero1 == 0):
        multiplos.append(numero)

for resultado in multiplos:
    print(f"El {resultado} es multiplo de {numero1}")

