"""En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoras que compre. Si las
computadoras son menos de cinco se les dará un 10% de descuento sobre
el total de la compra; si el número de computadoras es mayor o igual a
cinco pero menos de diez se le otorga un 20% de descuento; y si son 10 o
más se les da un 40% de descuento. El precio de cada computadora es de
$3.500.000"""

PRECIO_COMPUTADOR = 3500000
DESCUENTO_BASICO = 0.10
DESCUENTO_INTERMEDIO = 0.20
DESCUENTO_AVANZADO = 0.4

numero_computadores = int(input("Por favor ingrese la cantidad de computadores comprados: "))

if(numero_computadores < 5):
    total_compra = numero_computadores* PRECIO_COMPUTADOR
    total_compra_descuento = total_compra - (total_compra * DESCUENTO_BASICO )
    print(f"El valor total a pagar por sus {numero_computadores} es: {total_compra_descuento}")

elif(numero_computadores >= 5 and numero_computadores < 10):
    total_compra = numero_computadores* PRECIO_COMPUTADOR
    total_compra_descuento = total_compra - (total_compra * DESCUENTO_INTERMEDIO )
    print(f"El valor total a pagar por sus {numero_computadores} es: {total_compra_descuento}")

elif( numero_computadores >= 10):
    total_compra = numero_computadores* PRECIO_COMPUTADOR
    total_compra_descuento = total_compra - (total_compra * DESCUENTO_AVANZADO )
    print(f"El valor total a pagar por sus {numero_computadores} es: {total_compra_descuento}")


