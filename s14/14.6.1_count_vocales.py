vocales = "aeioucdef"
resultado = []

frase = input("Por favor ingrese la frase que desea verificar: ").lower()
print(frase)

for vocal in vocales:
    conteo_vocales = frase.count(vocal)
    mensaje = f"En la frase hay {conteo_vocales} veces la vocal {vocal}"
    resultado.append(mensaje)

for elemento in resultado:
    print(elemento)