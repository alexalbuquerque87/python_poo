class Pessoa:

    def andar(self):
        print('Estou andando' )

    def falar(self):
        print ('Estou falando')

class Cliente(Pessoa) :

    def comprar(self):
        print ('Estou comprando')

class Vendedor (Pessoa) :

    def vender(self):
        print ('Estou vendendo' )

c1 = Cliente()

print(c1)
c1.andar()
c1.comprar()
#c1.vender() #Error AttributeError: 'Cliente' object has no attribute 'vender'
c1.falar()