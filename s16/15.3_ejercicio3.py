"""Implementar que imprima el resultado de 2 elevado a las 0 hasta 2 elevado a las 30"""

potencias = []

for numero in range (0,31):
        potencias.append(2 **numero)

for resultado in range (len(potencias)):
    print(f"El resultado de: 2^{resultado}={potencias[resultado]}")

