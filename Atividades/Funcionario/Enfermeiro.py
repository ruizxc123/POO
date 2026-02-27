from FuncionarioSaude import FuncionarioSaude

class Enfermeiro(FuncionarioSaude):
    def __init__(self, nome, registro, salario, registro_conselho, setor):
        super().__init__(nome, registro, salario, registro_conselho)
        self.setor = setor
        
    def cacular_bonus(self):
        if self.salario > 0 and self.ativo:
            return self.salario * (15/100)
        return False
    
    def descricao_funcao(self):
        return print(f'Setor do enfermeiro(a): {self.setor}')
    
    def exibir_dados(self):
        super().exibir_dados()
        print('Setor:', self.setor)
        