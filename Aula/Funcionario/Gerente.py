from Funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor
    
    def calcular_bonus(self):
        return self.salario * 0.17
    
    #sobreescrevendo métodos e adicionado print n Setor
    def exibir_dados(self):
        super().exibir_dados()
        print('Setor: ', self.setor)