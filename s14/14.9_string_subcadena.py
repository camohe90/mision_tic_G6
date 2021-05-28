frase = "Bienvenidos a una nueva sesion del curso de python una version actualizada"

sub_cadena = input("Digite la frase que desea validar")

resultado = frase.find(sub_cadena) # busca en el string y retorna la posicion donde encuentra la subcadena que se envia como paramentro de la funcion.

print(resultado)