contador = 1
clientes = {
    1234: ["Camilo", "Molano", "Bogota"],
    4567: ["Alejandro", "Herrera", "Cali"],
    890: ["Daniel", "Gomez", "Tunja"],
    4689: ["Pilar", "Diaz", "Medellin"],
}

print(clientes[1234])
print(clientes[1234][2])

#print(clientes[9999])

resultado = clientes.get(1234)
print (resultado)

if(resultado):
    print(f"Cliente encontrado, es la informacion {resultado}")
else:
    print("Cliente no encontrado")

resultado = clientes.get(9999)

if(resultado):
    print(f"Cliente encontrado, es la informacion {resultado}")
else:
    print("Cliente no encontrado")

cedulas = tuple(clientes.keys())
print(cedulas)

informacion = tuple(clientes.values())
print(informacion)

for cliente in clientes:
    print(cliente)

for cliente in clientes.values():
    for datos in cliente:
        print(datos.upper(), sep=" ", end=" ")
    print()

for clave, valor in clientes.items():
    print(f"Esta es la cedula del cliente {contador} {clave} y esta es su informacion {valor}")
    contador +=1