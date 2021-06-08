numero_cedula = [1,2,3,4,5,6,7,8,9,10]
#print(contador)

try:
    print(contador)
except:
    print("Ocurrio un error")

try:
    numero = int(input("Digite un numero: "))
    print(numero *2) 
except:
    print("Error de tipo")

try:
    print(len(numero_cedula))
    print(numero_cedula[14]) 
except:
    print("Fuera de rango")

try:
    numero = 10 +"20"
except:
    print("No se puede realizar la operacion por el tipo")