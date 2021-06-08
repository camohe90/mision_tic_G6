factorial_n = 1
factorial_m = 1
factorial_n_m =1

numero_n = int(input("Ingrese por favor el numero n: "))
numero_m = int(input("Ingrese por favor el numero m: "))

while numero_n < numero_m:
    print("Por favor verifique que n sea mayor que m")
    numero_n = int(input("Ingrese por favor el numero n: "))
    numero_m = int(input("Ingrese por favor el numero m: "))

for numero in range(1, numero_n+1):
    factorial_n = factorial_n * numero

for numero in range(1, numero_m+1):
    factorial_m = factorial_m * numero

for numero in range(1, (numero_n-numero_m)+1):
    factorial_n_m = factorial_n_m * numero

combinatoria = factorial_n / (factorial_n_m * factorial_m)

print(f"La combinatoria es {combinatoria}")