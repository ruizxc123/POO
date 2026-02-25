class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def exibir_dados(self):
        print('\n Nome', self.nome)
        print('Salario R$ ', self.salario)
        
    def calcular_bonus(self):
        return self.salario * 0.1
    
        
    
    