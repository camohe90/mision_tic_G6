numero1 = 0
numero2 = 1

numero_fibonacci = int(input("Digite hasta que nunero de fibonacci desea conocer la secuencia: "))

while numero_fibonacci <= 0:
    print("Por favor ingrese un numero mayor a 0")
    numero_fibonacci = int(input("Digite hasta que nunero de fibonacci desea conocer la secuencia: "))

if numero_fibonacci ==1:
    print("Este es el primer numero de Fibonacci:", numero1 )

else:
    print("Esta es la secuencia de Fibonacci")
    for numero in range(0,numero_fibonacci):
        print(numero1)
        total = numero1 + numero2
        numero1 = numero2
        numero2 = total
