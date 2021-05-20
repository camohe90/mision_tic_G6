"""Un vendedor recibe un sueldo base, mas un 10% extra por comisión de
sus ventas, el vendedor desea saber cuanto dinero obtendrá por
concepto de comisiones por las tres ventas que realiza en el mes y el
total que recibirá en el mes tomando en cuenta su sueldo base y
comisiones."""

PORCENTAJE_COMISION = 0.10

salario_base = float(input("Ingres su sueldo base: "))
ventas = float(input("ingrese el total de las ventas"))
comisiones = ventas * PORCENTAJE_COMISION
salario_total = salario_base + comisiones

print(f"Sus comisiones estes mes son: {comisiones}")
print(f"Su salario total este mes es: {salario_total}")

