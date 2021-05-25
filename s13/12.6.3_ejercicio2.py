suma = 0
total_ventas = 0

mensaje = ( 
    "Ingrese el costo de los productos que desea totalizar ")

venta = int(input(mensaje))

while(venta != 0 ):
    if(venta > 0):
        total_ventas = total_ventas + venta   
    venta = int(input("Ingrese el costo de los productos: "))

if total_ventas > 1000:
    total_ventas = total_ventas - total_ventas * 0.1
    print(f"El total de tus compras es {total_ventas}")
else:
    print(f"El total de tus compras es {total_ventas}")
