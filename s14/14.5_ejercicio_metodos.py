nombre = input("Digite su nombre completo: ")

print(f"Su nombre compledo es {nombre}")

lista_nombre = nombre.split()
print(lista_nombre)
union = "".join(lista_nombre)
print(union)
cantidad_caracteres = len(union)
print(f"La cantidad de letras que tiene su nombre es {cantidad_caracteres}")