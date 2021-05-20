precio_producto_x = 1000
precio_producto_y = 1000
precio_producto_z = 1000

#Calculo los ingresos teniendo en cuenta el margen de utilidad de cada producto
ingresos_de_ventas = precio_producto_x*1.20 + precio_producto_y*1.30 + precio_producto_z*1.40

print(ingresos_de_ventas)


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


O = 2
I = 3 