numeros = [1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5]

promedio = (numeros[10] + numeros[11] + numeros[12] + numeros[13] + numeros[14]) / 5
promedio_2 = sum(numeros[10:15]) / 5
print(promedio)
print(promedio_2)




numeros.insert(15, promedio)

print(numeros)

