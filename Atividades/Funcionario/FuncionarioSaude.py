from Funcionario import Funcionario

class FuncionarioSaude(Funcionario):
    def __init__(self, nome, registro, salario, registro_conselho):
        super().__init__(nome, registro, salario)
        self.registro_conselho = registro_conselho
        
    def validar_registro(self):
        print('Isso aí')
        

        