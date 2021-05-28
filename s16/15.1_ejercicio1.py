"""Implementar un programa que se muestren todos los multiplos de 6 entre 6 y 150 
    ambos inclusive"""

multiplos = []

for numero in range (6,151,1):
    if(numero % 6 == 0):
        multiplos.append(numero)

for resultado in multiplos:
    print(f"El {resultado} es multiplo de 6")

