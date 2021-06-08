"""Solicitar al usuario que ingrese una lista de numero, digite x para finalizar y que ingrese un numero   que desea limite, con ese limite desea saber numeros hay menor que este en la lista original y generar un lista con esos numeros"""

numero = 0
numeros_ingresados = []


def numeros_menores(numeros, numero_limite):
    menores =[]
    del numeros[-1]

    for datos in numeros:
        if(int(datos) < numero_limite):
            menores.append(int(datos))
    return menores


while numero != "x":
    numero = input("Digite el numero que desea almacenar: ")
    numeros_ingresados.append(numero)
print("***Numeros ingresados correctamente***")

limite = int (input("Digite el numero que desea validar: "))

numeros_menores_funcion = numeros_menores(numeros_ingresados, limite)

print(f"Los numeros menores que {limite} son {numeros_menores_funcion}")