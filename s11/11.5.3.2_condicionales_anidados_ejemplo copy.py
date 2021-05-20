numero1 = int(input("Ingrese el numero1: "))
numero2 = int(input("Ingrese el numero2: "))

if numero1 == numero2:
    resultado = numero1 * numero2
    print(f"El resultado es: {resultado}")
elif numero1 > numero2:
    resultado = numero1 - numero2
    print(f"El resultado es: {resultado}")
else:
    resultado = numero1 + numero2
    print(f"El resultado es: {resultado}")