numero1 = 25.9
numero2 = 10
palabra = "Hola"

validar = isinstance(numero1, float)
print(validar)

validar = isinstance(numero1, int)
print(validar)

validar = isinstance(numero2, int) # Retorna True si el primer parametro es del mismo tipo que el segundo
print(validar)

validar = isinstance(palabra, str)
print(validar)