class Pessoas:
    possui_boca = True
    raca = 'Ser humano'

    #__init__ sempre é chamado na classe
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f'{self.retorna_nome()} está logando no sistema')

    def retorna_nome(self):
        return self.nome
    
    @classmethod
    def andar(cls):
        print(cls)
        cls.possui_boca = False
        return None
    
    @staticmethod
    def is_adult(idade):
        if idade > 18:
            return True
        return False

p1 = Pessoas('João Silva', 23, '123.456.780-01')

p1.logar_sistema()
print(p1.raca)

#Método de classe
print(f'possui_boca = {Pessoas.possui_boca}')
Pessoas.andar()
print(f'possui_boca = {Pessoas.possui_boca}')

#Método estático
print(f'is_adult = {Pessoas.is_adult(21)}')