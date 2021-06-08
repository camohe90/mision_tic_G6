from random import choice


numeros = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
palos = ("Picas","Corazones","Treboles","Diamantes")

test_poker = ["A Picas", "A Corazones", "A Treboles", "A Diamantes", "K Diamantes"]

baraja = []
cartas_elegidas = []


def poker(cartas_validar):
    cartas_sin_palos = []


    for carta in cartas_validar:
        cartas_sin_palos.append(carta[0][0])
    print (cartas_sin_palos)
    
    for carta in cartas_sin_palos:
        if cartas_sin_palos.count(carta) >=4:
            return "Hay poker"
        else:
            return "No hay poker"
        


for palo in palos :
    for numero in numeros:
        carta = numero + " " + palo
        baraja.append(carta)
print(baraja)


baraja_cartas = tuple(baraja)

for elegir_carta in range(5):
    cartas_elegidas.append(choice(baraja_cartas))

print(f"En la mano {cartas_elegidas} {poker(cartas_elegidas)}")

print(f"En la mano {test_poker} {poker(test_poker)}") 




