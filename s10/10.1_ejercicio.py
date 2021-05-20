numeros = [1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5]

promedio = (numeros[10] + numeros[11] + numeros[12] + numeros[13] + numeros[14]) / 5
print(promedio)

varianza1 = ((numeros[10] - promedio) ** 2) / 5
varianza2 = ((numeros[11] - promedio) ** 2) / 5
varianza3 = ((numeros[12] - promedio) ** 2) / 5
varianza4 = ((numeros[13] - promedio) ** 2) / 5
varianza5 = ((numeros[14] - promedio) ** 2) / 5

varianza_total = varianza1 + varianza2 + varianza3 + varianza4 + varianza5

numeros.insert(15, varianza_total)

print(varianza_total)
print(numeros)
