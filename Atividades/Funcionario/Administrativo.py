from Funcionario import Funcionario

class Administrativo(Funcionario):
    def __init__(self, nome, registro, salario, departamento):
        super().__init__(nome, registro, salario)
        self.departamento = departamento
        
    def cacular_bonus(self):
        if self.salario > 0 and self.ativo:
            return self.salario * (10/100)
        return False
    
    def descricao_funcao(self):
        return print(f'Departamento do Administrativo {self.nome} é {self.departamento}')
    
    def exibir_dados(self):
        super().exibir_dados()
        print('Departamento:', self.departamento)
    