"""Realizar un programa que simule a una persona que saluda a otra, deben solicitar que el usuario ingrese nombre, apellido, comida favorita y color favorito. El sistema debe imprimir dos mensajes. 1 Saludando al usuario, 2 Diciendo algun comentario referente a la comida y al color ingresado"""

print("Manejo de información de entrata con python")
print("--------------------------------------------------")
primer_nombre = input("Por favor ingrese su nombre: ")  #Guardo la información ingresada por teclado  en la variables primer_nombre
primer_apellido = input("Por favor ingrese su apellido: ") #Guardo la información ingresada por teclado  en la variables primer_apellido
comida = input("Por favor ingrese tu comida favorita: ")
color = input("Por favor ingrese tu color favorito: ")

print("Hola", primer_nombre,primer_apellido,"es un gusto saludarte")
print("A mi tambien me gusta la", comida ,"pero mi color favorito no es el", color , "es el verde")

print(type(primer_nombre))
print(type(primer_apellido))
print(type(comida))
print(type(color))