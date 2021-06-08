

def recibir_data(mensaje, tipo):
    validar = True
    while validar:
        try:
            dato = tipo(input(mensaje))
        except ValueError:
            print(f"Por favor verificar que el dato ingresado sea de tipo {tipo}")
        else:
            validar = False
            return dato

edad = recibir_data("Por favor ingrese la edad: ",int)
print(f"Esta es la edad ingresada {edad} {type(edad)}")

peso =  recibir_data("Por favor ingrese su peso", float)
print(f"Este es el peso ingresado {peso} {type(peso)}")

nombre =  recibir_data("Por favor ingrese su nombre", str)
print(f"El nombre ingresado es {nombre} {type(nombre)}")

