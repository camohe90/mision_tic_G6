frutas = [ "Lulo" , "Pera", "Manzana", "Piña", "Kiwi", "Guanábana", "Banano", "Pomelo"]
frutas2 = ("Lulo" , "Pera", "Manzana", "Piña", "Kiwi", "Guanábana","Banano","Pomelo")

numeros = [10,4,6,7,12,56,8]
numeros2 = (10,4,6,7,12,56,8)

varios_elementos = ["hola", [2,3,4], 10.5]

print(frutas[2], frutas2[2])
print(numeros[2:6], numeros2[2:6])

print(min(frutas), "," , min(frutas2))
print(max(frutas), "," , max(frutas2))

frutas.append("Uva")
print(frutas)

#frutas2.append("Uva")  No puedo agregar elementos a una tupla
#print(frutas2)

lista_ordenada = sorted(frutas)
tupla_ordenada = sorted(frutas2)

frutas.sort()
print(frutas)

''' frutas2.sort()
print(frutas2)
 '''
menu_definitivo = tuple(frutas)

print(menu_definitivo)

