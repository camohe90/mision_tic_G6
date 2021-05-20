#Comentarios de una linea antes de la función
def funcion(primer_parametro, segundo_paramtero):
    """Sirve para describir que hace la función
    
    primer_parametro -- Descripcion del primer parametros
    segundo_paraemtro -- Descripcion del segundo"""


def cuadratica(a,b,c, x):
        """Resolver ecuaciones cuadraticas mediante la formula que tiene la
        siguiente forma:
        ax**2  + bx + c = 0
        Siempre voy a tener dos soluciones x_1 y x_2"""

    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)

    return x_1, x_2