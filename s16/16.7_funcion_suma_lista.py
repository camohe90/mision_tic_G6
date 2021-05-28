def sumar(numeros):
    """Esta funcion retorna la sumatoria de los elementos de una lista
        
        Parametros:
        numero: lista

        Return:
        numero: int sumatoria de los elemtos
    """
    suma = 0

    for numero in numeros:
        suma = suma + numero
    
    return suma


print(sumar([1,2,3,4,5,6,7,8,9,10]))