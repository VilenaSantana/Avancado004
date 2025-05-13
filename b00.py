class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer (self):
        print(f"{self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar (self):
        print(f"{self.nome} foi miando...")
    def comer(self):
        print(f"{self.nome} foi tomar seu leitinho...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mu (self):
        print(f"{self.nome} fez Muuuuuuuuuuu...")
    def comer (self):
        print(f"{self.nome} foi comer capim...")

class Galinha(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def grita (self):
        print(f"{self.nome} gritou Cocoricooooooo...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir (self):
        print(f"{self.nome} foi latindo...")

class Rato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def roer (self):
        print(f"{self.nome} foi roendo o queijo...")


class