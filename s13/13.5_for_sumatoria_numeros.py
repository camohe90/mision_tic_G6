numeros_usuario = [1,2,3,4,5,6,7,8,9,10,11]
suma = 0
suma2 = 0

cantidad_elementos = len (numeros_usuario)

for numero in range(0,cantidad_elementos,2):
    suma = suma + numeros_usuario[numero]

print("La suma de los elementos en las posciones pares del arreglo es:", suma)

for numero in range(1,cantidad_elementos,2):
    suma2 = suma2 + numeros_usuario[numero]

print("La suma de los elementos en las posciones impares del arreglo es:", suma2)
