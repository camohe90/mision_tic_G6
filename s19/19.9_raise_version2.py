

direcciones =[1,2,3,4,5,6,7,8]

def agregar_datos(lista, elemento):
    if elemento in lista:
        raise ValueError(f"ERROR -> No se pueden añadir elementos duplicados {elemento}", "ERROR456")
    lista.append(elemento)

try:
    agregar_datos(direcciones,9)
except ValueError as error:
    print(error.args)
else:
    print("Elementos agregados correctamente")
finally:
    print(f"La lista de resultante es {direcciones}")


try:
    agregar_datos(direcciones,3)
except ValueError as error:
    print(error.args)
else:
    print("Elementos agregados correctamente")
finally:
    print(f"La lista de resultante es {direcciones}")
