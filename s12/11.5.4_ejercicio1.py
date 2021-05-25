"""Determinar la cantidad de dinero que recibirá un trabajador por
concepto de las horas extras trabajadas en una empresa, sabiendo
que cuando las horas de trabajo exceden de 40, el resto se
consideran horas extras y que estas se pagan al doble de una hora
normal cuando no exceden de 8; si las horas extras exceden de 8 se
pagan las primeras 8 al doble de lo que se pagan las horas normales
y el resto al triple"""


horas_trabajadas_mes = int(input("Por favor ingrese la cantidad de horas trabajadas: "))
VALOR_HORA = input("Por favor el valor por hora: ")


if (horas_trabajadas_mes<=40):
    salario = horas_trabajadas_mes*10000
    print(f"El salario del mes es: {salario}")
elif (horas_trabajadas_mes>40 and  horas_trabajadas_mes<=48):
    horas_recargo = horas_trabajadas_mes - 40
    print("Horas de recargo", horas_recargo)
    total_horas_extra = (horas_recargo * (VALOR_HORA*2))
    total_salario = (horas_trabajadas_mes - horas_recargo) * VALOR_HORA + total_horas_extra
    print(f"La cantidad de dinero que recibirá por concepto de horas extra es {total_horas_extra} y el total de su salario es: {total_salario}")
elif (horas_trabajadas_mes >= 48):
    horas_triple = horas_trabajadas_mes - 48
    horas_dobles = 8
    print("horas triples", horas_triple, "horas_dobles", horas_dobles)
    total_horas_extra = (horas_dobles * VALOR_HORA*2) + (horas_triple * (VALOR_HORA*3))
    total_salario = (horas_trabajadas_mes - horas_triple - horas_dobles) * VALOR_HORA + total_horas_extra

    print(f"La cantidad de dinerp que recibirá por concepto de horas extra es {total_horas_extra} y el total de su salario es: {total_salario}")

