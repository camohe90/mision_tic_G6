vocales = "aeiou"
contador = 0

frase = input("Por favor ingrese la frase que desea verificar: ")

for letra in frase:
    if letra in vocales:
        contador+=1

print(f"En esta frase: {frase}\nhay {contador} vocales")