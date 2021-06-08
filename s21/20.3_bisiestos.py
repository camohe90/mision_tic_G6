def dias_anio(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return 366
    else:
        return 365

print(dias_anio(2002))
print(dias_anio(2004))
print(dias_anio(1900))
print(dias_anio(2000))