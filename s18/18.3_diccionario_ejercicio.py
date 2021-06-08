from os import system

system("cls")

consultar = True

agenda_telefonos = {
    "Alejandro" : 4567,
    "Daniel" : 89012,
    "Pilar" : 5678,
    "Jairo" : 76453,
    "Camilo" : 4556465
}

mensaje = (
    "-----------------------------------------------------------\n"
    "Bienvenidos a la agenda de telefonos de python mision TIC\n"
    "-----------------------------------------------------------\n"
    "Usted cuenta con las siguientes opciones \n"
    "1. Consultar contacto\n"
    "2. Añadir contacto\n"
    "3. Modificar contacto\n"
    "4. Borrar contacto\n"
    "5. Salir\n"

)

while consultar:
    print(mensaje)
    opcion = input("Por favor elija una de las opciones definidas: ")

    while opcion not in ("1","2","3","4","5"):
        opcion = input("Por favor elija una opcion valida")
    
    if opcion == "1":
        nombre = input("Por favor digite el nombre que desea consultar: ")
        if nombre not in agenda_telefonos:
            print("---------------------------------------------------")
            print("El nombre ingresado no se encontró en su agenda: ")
        else:
            telefono = agenda_telefonos[nombre]
            print("---------------------------------------------------")
            print(f"Encontramos la siguente informacion en su agenda:\n{nombre} : {telefono}")
        
    elif opcion == "2":
        nombre = input("Por favor digite el nombre que desea consultar: ")
        if nombre in agenda_telefonos:
            print("---------------------------------------------------")
            print("El nombre ingresado ya se encuentra en su agenda: ")
        else:
            telefono = int(input("Por favor ingrese el numero de telefono"))
            agenda_telefonos[nombre] = telefono
            print("---------------------------------------------------")
            print("El contacto se guardo correctamente: ")
    
    elif opcion == "3":
        nombre = input("Por favor digite el nombre que desea modificar: ")
        if nombre not in agenda_telefonos:
            print("---------------------------------------------------")
            print("El nombre ingresado no se encontró en su agenda: ")
        else:
            telefono = int(input("Por favor ingrese el nuevo numero de telefono"))
            agenda_telefonos[nombre] = telefono
            print("---------------------------------------------------")
            print("El contacto se actualizo correctamente: ")
    
    elif opcion == "4":
        nombre = input("Por favor digite el nombre que desea borrar: ")
        if nombre not in agenda_telefonos:
            print("---------------------------------------------------")
            print("El nombre ingresado no se encontró en su agenda: ")
        else:
            del agenda_telefonos[nombre]
            print("---------------------------------------------------")
            print("El contacto se elimino correctamente: ")
    
    elif opcion == "5":
        consultar = False

print("Finalice el programa")