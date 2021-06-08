edad = 0



def recibar_datos():
    global edad

    while True:
        try:
            edad = int(input("digite su edad"))
        except ValueError:
            print("Por favor verifique que todos lo datos ingresados sean de tipo numerico")
        else:
            print("-------------------Informacion ingresada correctamente------------------")
            break
        finally:
            print("Acá finalizan las validaciones")

print(edad)
recibar_datos()
print(edad)

