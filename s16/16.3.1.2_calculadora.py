
def imprimir(resultado, operacion):
    return f"El resultado de la {operacion} es: {resultado}"

def sumar(numero_1, numero_2):
    resultado_suma = numero_1 + numero_2
    return imprimir(resultado_suma, "suma")

def multiplicar(numero1, numero2):
    resultado_multiplicacion = numero1 * numero2
    return imprimir(resultado_multiplicacion, "multiplicacion")

def dividir(numero1, numero2):
    resultado_division = numero1 / numero2
    return imprimir(resultado_division, "division")

def restar(numero1, numero2):
    resultado_resta = numero1 - numero2
    return imprimir(resultado_resta, "resta")
    

numero1 = int(input("Digite el numero 1: "))
numero2 = int(input("Digite el numero2: "))

print(sumar( numero1, numero2))
print(multiplicar( numero1, numero2))
print(dividir( numero1, numero2))
print(restar( numero1, numero2))