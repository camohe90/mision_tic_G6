edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Bienvenido ud puede ingresar")
else:
    tiempo_restante = 18 - edad
    print("Por el momento ud no puede ingresar, por favor intentelo en", tiempo_restante, "años")
    
print("Gracias por usar nuestro programa")
