class Hospital:
    def __init__(self):
        self.lista_funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append((funcionario))
    
    def listar_funcionarios(self):
        for f in self.lista_funcionarios:
            f.exibir_dados()
            
    def folha_pagamento(self):
        return sum(f.salario_total() for f in self.lista_funcionarios)
    
    def maior_salario(self):
        return max(self.lista_funcionarios)
    
    