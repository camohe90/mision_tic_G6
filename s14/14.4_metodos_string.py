frase = "Bienvenidos a una NUEVA sesion del curso de Python"

print(frase)
print(type(frase))
print(len(frase))

print(frase.upper()) # Retorna el string todos sus caracteres en mayuscula
print(frase.lower())# Retorna el string todos sus caracteres en minuscula

print(frase.replace("Python", "cocina")) #busca en el string que se encuentre la palabra que esta en el primer parametro y si lo encuentra lo reemplaza por el segundo parametro

print(frase.title()) # Retorna el string con todas las palabras iniciando con mayuscula

palabra5 = "perro"
print(palabra5 >= "Perro".lower())

palabras = frase.split() # Creo un lista con las palbras que se encuentran en el string frase y se separan por el espacio
print(palabras)

print(" ".join(palabras))# Uno los elementos del string por el caracter que deje entre las " "


for palabra in palabras:
    print(palabra.capitalize(), end=" ")
print()

print(palabras)


