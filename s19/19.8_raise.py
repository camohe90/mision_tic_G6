numero = int(input("Ingrese un numero"))

try:
    if numero < 10:
        raise ValueError("Error -> numero menor al umbral definido")
except ValueError as errorcito:
    print("vamos a ver el error")
    print(errorcito.args[0])