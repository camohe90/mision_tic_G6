def sumar(numero_1, numero_2):
    resultado_suma = numero_1 + numero_2
    return f"El resultado de la suma es: {resultado_suma}"

def multiplicar(numero1, numero2):
    resultado_multiplicacion = numero1 * numero2
    return f"El resultado de la multiplicacion es: {resultado_multiplicacion}"

def dividir(numero1, numero2):
    resultado_division = numero1 / numero2
    return f"El resultado de la division es: {resultado_division:.2f}"

def restar(numero1, numero2):
    resultado_resta = numero1 - numero2
    return f"El resultado de la resta: {resultado_resta}"
    


numero1 = int(input("Digite el numero 1: "))
numero2 = int(input("Digite el numero2: "))

print(sumar( numero1, numero2))
print(multiplicar( numero1, numero2))
print(dividir( numero1, numero2))
print(restar( numero1, numero2))