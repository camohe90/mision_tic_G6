"""En una tienda de descuento se efectúa una promoción en la cual se hace un
descuento sobre el valor de la compra total según el color de la bolita que el
cliente saque al pagar en caja. Si la bolita es de color blanco no se le hará
descuento alguno, si es verde se le hará un 10% de descuento, si es amarilla un
25%, si es azul un 50% y si es roja un 100%. Determinar la cantidad final que el
cliente deberá pagar por su compra. se sabe que solo hay bolitas de los colores
mencionados."""

from random import choice

DESCUENTO_BLANCO = 0
DESCUENTO_VERDE = 0.1
DESCUENTO_AMARILLA = 0.25
DESCUENTO_AZUL = 0.5
DESCUENTO_ROJA = 1

bolitas = ["BLANCO", "VERDE", "AMARILLA","AZUL", "ROJA"]

total_compra = int(input("Por favor ingrese la valor de la compra: "))
color_bolita = choice(bolitas)

print(f"Uste saco la bolita de color {color_bolita}")

if color_bolita == "BLANCO":
    print(f"El valor a pagar es : {total_compra}")

elif color_bolita == "VERDE":
    total_compra_descuento = total_compra - (total_compra * DESCUENTO_VERDE)
    print(f"El valor a pagar es : {total_compra_descuento}")

elif color_bolita == "AMARILLA":
    total_compra_descuento = total_compra - (total_compra * DESCUENTO_AMARILLA)
    print(f"El valor a pagar es : {total_compra_descuento}")

elif color_bolita == "AZUL":
    total_compra_descuento = total_compra - (total_compra * DESCUENTO_AZUL)
    print(f"El valor a pagar es : {total_compra_descuento}")
elif color_bolita == "ROJA":
    print(f"Usted obtuve el 100% de descuento en su cuenta")