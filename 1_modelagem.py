class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f'{self.nome} está logando no sistema')

p1 = Pessoas('João Silva', 23, '123.456.780-01')
p2 = Pessoas('Pedro Paulo', 39, '098.765.432-10')

p1.logar_sistema()
p2.logar_sistema()
