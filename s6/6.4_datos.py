num1 = 20
num2 = 10
num3 = -15
num4 = 53252342342345

print(num1)
print(type(num1))
print(num3)
print(type(num3))

numero_flotante = round(10 / 3, 4)
print(numero_flotante)
print(type(numero_flotante))
print(4.6e7)
print(type(4.6e7))
print(pow(4,7))
print(4**7)

x = 2 + 3j 
print(type(x))
print(x.real)
print(x.imag)

frase = "Esto es una cadena de texto"  #Esto es un string
print(frase)
print(frase[0])
print(frase[-1])
print(len(frase))

lista = [1,2,3,4,5,6,7,8,9,10] # son mutables
print(lista[0])
print(lista[-1])
print(lista[0:4])

lista2 = ["hola",1 , 2.2 , [3,2]]
print(lista2[2])
print(lista2[3][1])

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13] # son mutables
print(len(lista))
lista.append(14)
print(len(lista))
lista.append(15)
lista[0]=100
print(lista)

lista = [] 
resultado = 3 + 5
lista.append(resultado)
lista.append(resultado * 2)
lista.append(resultado + 1)
print(lista)
print(len(lista))

tupla = (1,2,3,4, "numeros") #son inmutables
print(tupla)
print(tupla[-1])
#tupla[1] = "Hola"

set_datos = {5,2,4,5,6,7,3,3,2,3,4,5,6,6}
print(set_datos)

futbolistas = {
    1 : "Ospina", 
    13 : "Mina",
    10 : "James", 
    5 : "Puyol",
    9 : "Falcao", 
    19 : "Muriel",
    11: "Cuadrado", 
    18 : "Fabra",
    6: "Barrios",  
    3: "Murillo",
    'defensa1' : "Zapata"
}

print(futbolistas[1])
print(futbolistas['defensa1'])




