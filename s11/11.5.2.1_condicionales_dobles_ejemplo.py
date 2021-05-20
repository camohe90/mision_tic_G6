"""Determinar si un alumno apruebao reprueba un curso, sabiendo
    que aprobara si su promedio detres calificaciones es mayor o
    igual a 70; reprueba en caso
    contrario."""

calificacion_1, calificacion_2, calificacion_3 = input("Ingrese las tres calificaciones parciales separadas por espacio").split()

promedio = ((float(calificacion_1) + float(calificacion_2) + float(calificacion_3)) /3 ) 

if promedio >= 70:
    print("El alumno aprobo")
else:
    print("El alumno reprobo")

