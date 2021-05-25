frase = "Bienvenidos a una NUEVA sesion del curso de Python"

print(frase)
print(type(frase))
print(len(frase))

print(frase.upper())
print(frase.lower())

print(frase.replace("Python", "cocina"))

print(frase.title())

palabra5 = "perro"
print(palabra5 >= "Perro".lower())

palabras = frase.split()
print(palabras)

print(" ".join(palabras))


for palabra in palabras:
    print(palabra.capitalize(), end=" ")
print()

print(palabras)


