notas = [3,4,5,3,2,3,4,5,4,3,4,5,2,1,2,3]
total = 0

for nota in notas:
    total = total + nota

promedio = total / len(notas)
print(f"Este es el promedio de las notas {promedio:.2f}")