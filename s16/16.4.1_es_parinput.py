def es_par(numero_validar):
    if numero_validar % 2 == 0:
        return "Es par"
    else: 
        return "No es par"

for numeros in range(5):
    numero_entrada = int(input("Por favor digite el numero que desea validar: "))
    print("El numero", numero_entrada, es_par(numero_entrada))
