class Pessoas:

    #__init__ sempre é chamado na classe
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f'{self.retorna_nome()} está logando no sistema')

    def retorna_nome(self):
        return self.nome

p1 = Pessoas('João Silva', 23, '123.456.780-01')

p1.logar_sistema()
