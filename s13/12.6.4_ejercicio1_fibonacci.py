
cantidad_datos= int(input("Digite hasta que numero desea conocer de la secuencia de fibonacci "))

numero1, numero2 = 0, 1
cuenta = 0

if cantidad_datos <= 0:
    print("Por favor ingrese un numero positivo")
elif cantidad_datos == 1:
    print("Este es el primer numero de Fibonacci",numero1);
else:
    print("Secuencia Fibonacci:")
    while cuenta < cantidad_datos:
        print(numero1)
        total = numero1 + numero2
        numero1 = numero2
        numero2 = total
        cuenta += 1