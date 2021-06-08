vector1 = [-3, 5]
vector2 = [2, -4]
vector3 = [1, 2]
vector4 = [3, 4]
vector5 = [-2, 5]
vector6 = [1, 3]


def producto_escalar(vector1, vector2):
    suma = 0
    for numero in range(len(vector1)):
        resultado = vector1[numero] *  vector2[numero]
        suma = suma + resultado

    return suma


print(f"El producto escalar es {producto_escalar(vector1, vector2)}")

print(f"El producto escalar es {producto_escalar(vector3, vector4)}")

print(f"El producto escalar es {producto_escalar(vector5, vector6)}")