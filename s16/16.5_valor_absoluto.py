def valor_absoluto(numero):
    """Esta funcion retornar el valor absoluto

        Parametros:
        numero: float

        Return:
        numero: float con el valor absoluto
    """
    if numero > 0:
        return numero
    else:
        return -numero

numero_entrada = float(input("Digite el numero que desea obtener el valor absoluto: "))
print(f"El valor absoluto del {numero_entrada} es {valor_absoluto(numero_entrada)}")