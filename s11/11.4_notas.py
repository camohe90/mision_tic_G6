"""Un alumno desea saber cual será su calificación final en la materia de
Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
40% del promedio de sus tres calificaciones parciales, 50% de la
calificación del examen final y 10% de la calificación de un trabajo final."""

PORCENTAJE_CALIFICACIONES = 0.40
PORCENTAJE_EXAMEN = 0.50
PORCENTAJE_TRABAJO = 0.10

calificacion_1, calificacion_2, calificacion_3 = input("Ingrese las tres calificaciones parciales separadas por espacio").split()

examel_final, trabajo_final = input("ingrese la nota del examen final seguida de la nota del trabajo final separado por un espacio").split()

nota_calificaciones = ((float(calificacion_1) + float(calificacion_2) + float(calificacion_3)) /3 ) * PORCENTAJE_CALIFICACIONES
nota_examen_final = float(examel_final) * PORCENTAJE_EXAMEN
nota_trabajo_final = float(trabajo_final) * PORCENTAJE_TRABAJO
nota_definitiva = nota_calificaciones + nota_examen_final + nota_trabajo_final

print(f"Su calificacion final es {nota_definitiva}")

