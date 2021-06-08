

try:
    resultado = 14 +"30"
except TypeError:
    print("ERROR-> Intento de sumar un numero y un string")
else:
    print("Operacion realizada correctamente")
finally:
    print("Pase lo que pase yo me voy a ejecutar y soy el cierre del try")


try:
    resultado = 14 + 30
except TypeError:
    print("ERROR-> Intento de sumar un numero y un string")
else:
    print("Operacion realizada correctamente")
finally:
    print("Pase lo que pase yo me voy a ejecutar y soy el cierre del try")