frase = input("Digite su numero de celular: ")
print(frase.isdigit())
if frase.isdigit():
    print("Ingreso correctamente el numero")
else: 
    print("No se ingreso correctamente el numero, ya que tiene letras o caracteres no validos")