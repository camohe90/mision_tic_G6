"""Factorial """


factorial = 1
numero_factorial = int(input("Digite el numero del cual desea conocer el factoria"))

for numero in range(1,numero_factorial+1):
    factorial = factorial * numero

print(f"El factoria de {numero_factorial} es {factorial}")



