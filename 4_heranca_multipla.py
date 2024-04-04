class Animal:
    def andar(self):
        print('animal andando')

    def correr(self):
        print('estou correndo')

    def pular(self):
        print('estou pulando')

class Mamifero:
    def mamifero(self):
        print('eu sou um mamífero')
    
    def pelagem(self):
        print('não definido')

class Felino(Animal):
    def felino(self):
        print('eu sou um felino')

    def pelagem(self):
        print('eu tenho pelos')

class Gato(Felino, Mamifero):
    def miar(self):
        print('estou miando')

g1 = Gato()
g1.andar()
g1.felino()
g1.mamifero()
g1.pelagem() #exibe o método do felino, pois felino vem primeiro na ordem herdada por gato