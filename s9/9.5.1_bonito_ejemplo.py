CONSTANTE = "inicio"


def mi_funcion(a):
    return a + 4


class Perro:
    peso = 1.7

    def ladra(self):
        print("guau")

    def come(self):
        if self.peso < 1.5:
            self.peso = 1.9
        else:
            self.peso += 0.2

        print("Guau - que rico!")
