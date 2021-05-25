nombre = input("Digite su primer nombre")

while not(nombre.isalpha()):
    print("No se ingreso correctamente el nombre , ya que tiene caracteres o numero ")
    nombre = input("Digite su primer nombre")

print(f"Hola {nombre} es un gusto saludarte")