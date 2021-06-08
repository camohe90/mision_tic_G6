from sys import exc_info

try:
    numero = int(input("Digite un numero: "))
    print("El resultado de la division es", 1/numero)
except ZeroDivisionError:
    print("Hay una division entre cero")
    error = exc_info()
    print(type(error))
    print(error[0])
except:
    print("Ocurrio otro error")
