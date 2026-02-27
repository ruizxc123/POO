from FuncionarioSaude import FuncionarioSaude


class Medico(FuncionarioSaude):
    def __init__(self, nome, registro, salario, registro_conselho, especialidade):
        super().__init__(nome, registro, salario, registro_conselho)
        self.especialidade = especialidade
        
    def cacular_bonus(self):
        if self.salario > 0 and self.ativo:
            return self.salario * (20/100)
        return False
    
    def descricao_funcao(self):
        return print(f'Função do médico: {self.especialidade}')
    
    def exibir_dados(self):
        super().exibir_dados()
        print('Registro do conselho', self.registro_conselho)
        print('Especialidade', self.especialidade)