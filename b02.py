class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def custo (self):
        print(f"O valor do ingresso é {self.valor}")

class Vip(Ingresso):
    def __init__(self, adicinal):
        super().__init__(adicinal)
        self.valor *= 1.5
    def custo (self):
        print(f"O valor do ingresso vip é {self.valor}")

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calArea(self,base,altura):
        self.area=base*altura
        print(f"A area do retangulo é {self.area}")