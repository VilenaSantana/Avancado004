class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()


    def calculaArea(self,base, altura):
        self.area = base * altura
        print(f"A area do retangulo é {self.area}")

    def calculaPerimetro (self, base, altura):
        self.perimetro = (base+ altura)*2
        print(f"A perimetro do retangulo é {self.perimetro}")


class Triangulo(Forma):
    def __init__(self, calA, calP, altura):
        super().__init__(calA, calP, altura)