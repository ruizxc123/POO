class Hospital:
    def __init__(self):
        self.lista_funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append((funcionario))
    
    def listar_funcionarios(self):
        for f in self.lista_funcionarios:
            f.exibir_dados()
            
    def folha_pagamento(self):
        if not self.lista_funcionarios:
            return 
        return sum(f.salario_total() for f in self.lista_funcionarios)
    
    def maior_salario(self):
        if not self.lista_funcionarios:
            return 
        funcionario = max(self.lista_funcionarios, key=lambda f: f.salario_total())
        return f'Nome do funcionário : {funcionario.nome}, Salário total: {funcionario.salario_total()}'
    