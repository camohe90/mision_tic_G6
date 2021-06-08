numeros = [1,2,3,4]

from sys import exc_info

try:
    numero = int(input("Digite un numero: "))
    print("El resultado de la division es", 1/"hola")
except (ValueError, TypeError, IndexError):
    print("Tiene un error al introducir los datos")
    error = exc_info()
    print(error)
except ZeroDivisionError:
    print("Hay una division entre cero")
    error = exc_info()
    print(type(error))
    print(error[0])
except:
    print("Ocurrio un error")
    error = exc_info()
    print(type(error))
    print(error[0])

