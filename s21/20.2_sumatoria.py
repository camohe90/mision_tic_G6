def sumatoria(numero1, numero2):
    suma = 0
    for numero in range(numero1, numero2+1):
        #suma = suma + numero
        suma += numero
    return suma

print(sumatoria(1,10))