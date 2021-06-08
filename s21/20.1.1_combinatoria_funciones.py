def factorial(limite):
    resultado = 1
    for numero in range(1, limite+1):
        resultado = resultado * numero
    return resultado

def combinatoria(numero1, numero2):
    resultado = factorial(numero1) / (factorial(numero1-numero2) * factorial(numero2))
    return resultado

numero_n = int(input("Ingrese por favor el numero n: "))
numero_m = int(input("Ingrese por favor el numero m: "))

while numero_n < numero_m:
    print("Por favor verifique que n sea mayor que m")
    numero_n = int(input("Ingrese por favor el numero n: "))
    numero_m = int(input("Ingrese por favor el numero m: "))

resultado_combinatoria = combinatoria(numero_n, numero_m)
print("El resultado es", resultado_combinatoria)