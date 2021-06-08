vector1 = [4, -1]
vector2 = [2, 8]

vector3 = [-5, 3, 7]
vector4 = [6, -8, 2]


def ortogonales(vector1, vector2):
    suma = 0
    for numero in range(len(vector1)):
        resultado = vector1[numero] *  vector2[numero]
        suma = suma + resultado
    
    if suma == 0:
        return "son ortogonales"
    else:
        return "no son ortogonales"


print(f"El vector: {vector1} y el vector {vector2} {ortogonales(vector1, vector2)}")

print(f"El vector: {vector3} y el vector {vector4} {ortogonales(vector3, vector4)}")

