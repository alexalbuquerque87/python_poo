class Pessoa:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def andar(self):
        print('Estou andando')

    def falar(self):
        print ('Estou falando')

class Cliente(Pessoa) :

    def __init__(self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente

    def comprar(self):
        print ('Estou comprando')

    def andar(self): #ignora andar de Pessoa caso exista em cliente
        print('Andando sobreposto')

    def falar(self):
        super().falar() #super() chama a classe pai
        print('Estou gritando')

c1 = Cliente(2, 'João Silva', '123456789')
print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)

c1.andar()
c1.falar()