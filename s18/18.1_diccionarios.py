agenda_telefonos = {
    "Alejandro" : 4567,
    "Daniel" : 89012,
    "Pilar" : 5678,
    "Jairo" : 76453,
    "Camilo" : 4556465
}

agenda_telefonos2 = {
    "Alejandro" : 4567,
    "Daniel" : 89012,
    "Pilar" : 5678,
    "Jairo" : 76453,
    "Camilo" : 4556465
}

print(agenda_telefonos == agenda_telefonos2)
print(len(agenda_telefonos2))

print(agenda_telefonos)
print(agenda_telefonos["Camilo"])
telefono_jairo = agenda_telefonos["Jairo"]
print(telefono_jairo)

nuevo_telefono_camilo = 3016252610
agenda_telefonos["Camilo"] = nuevo_telefono_camilo
print(agenda_telefonos["Camilo"])

agenda_telefonos.pop("Daniel")
print(agenda_telefonos)

"""Tener cuidado de eliminar claves que ya no estan en el diccionario
del agenda_telefonos["Daniel"]"""

agenda_telefonos["CamiLo"] = 5555
print(agenda_telefonos)

