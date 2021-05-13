numeros = [10,4,5,6,7,8,9,4,5,6,7,9]

print(len(numeros))  #Cantidad de elementos que hay en una lista
print(numeros[-1]) #imprimimos el ultimo elementos de lista
ordenados = sorted(numeros) # organizamos los datos de menor a mayor y los guardamos en la varibale ordenados
print(ordenados)
numeros.append(100) #agrego a lista numeros un 100 al final
print( numeros)
print(len(numeros))
numeros.insert(2,240) #agrego a la lista numeros un 200 en la posicion 2
print(numeros)
numeros.pop(2)  #elimino el elemento que se encuentre en la posicion 2
print(numeros)
del numeros[2:4]
print(numeros)
print(numeros.index(10))

numeros_no_repetidos = set(numeros)
print(list(numeros_no_repetidos))