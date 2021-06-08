resultado = []
resultado2 = []

numero1 = [1,2,3,4,5]
numero2 = [1,2,3,4,5]

for elemento in range (len(numero1)):
    suma_listas = numero1[elemento] + numero2[elemento]
    resultado.append(suma_listas)

print(resultado)


for elemento in range (len(numero1)):
    suma_listas = numero1[elemento] + numero2[len(numero1)-1- elemento]
    resultado2.append(suma_listas)

print(resultado2)

