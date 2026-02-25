from  Funcionario import Funcionario

class Estagiaro(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.meses_contrado = 6
        
    # sobreescrevendo métodos para salario
    def calcular_bonus(self):
        return self.salario * 0.8
    
    # criando metodo especifico para Estagiario
    def renovar_contrato(self):
        self.meses_contrado += 6
        print('Contrato de Estagiario renovado')