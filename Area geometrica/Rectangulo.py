from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color): 

    def __init__ (self, lado1, lado2, color):
        FiguraGeometrica.__init__(self, lado1, lado2)
        Color.__init__(self, color)
    
    def calcular_area (self):
        return self.lado1 * self.lado2
      
    def __str__ (self):
        return f'''Ancho de cuadrado: {self.lado1}
alto de cuadrado: {self.lado2}
color: {self._color}
'''