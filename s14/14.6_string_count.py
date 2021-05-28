frase = "Seguimos aprendiendo a contar caracteres en python"
letra = input("Digite la letra que desea contar: ")

repeticion = frase.count(letra) #cuanta cuantas veces se repite en el string el parametro que se pase en los parentesis
repeticion2 = frase.count(letra,0,10)
print(f"La letra {letra} se repite {repeticion} veces en la frase")
print(f"La letra {letra} se repite {repeticion2} veces en el fragmento de la frase que ud definio")