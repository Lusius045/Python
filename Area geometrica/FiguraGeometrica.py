class FiguraGeometrica:
    def __init__(self, lado1, lado2):
        self._lado1 = lado1
        self._lado2 = lado2

    @property 
    def lado1(self):
        return self._lado1
    
    @lado1.setter
    def lado1(self, lado1):
        self._lado1 = lado1

    @property 
    def lado2(self):
        return self._lado2
    
    @lado2.setter 
    def lado2(self, lado2):
        self._lado2 = lado2

