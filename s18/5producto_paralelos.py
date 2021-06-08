vector1 = [6, -18]
vector2 = [-4, 12]



def ortogonales(vector1, vector2):
    suma = 0
    resultados = []


    for numero in range(len(vector1)):
        resultados.append(vector1[numero]  /  vector2[numero])
    
    if  resultados[0] == resultados[1]:
        return "son paralelos"
    else:
        return "no son paralelos"


print(f"El vector: {vector1} y el vector {vector2} {ortogonales(vector1, vector2)}")

