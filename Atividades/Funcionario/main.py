from Funcionario import Funcionario
from FuncionarioSaude import FuncionarioSaude   
from Hospital import Hospital
from Enfermeiro import Enfermeiro
from Medico import Medico
from Administrativo import Administrativo

def main():
    
    funcionario1 = Medico('Rui', 111, 10000, 222, 'Pediatrico')
    funcionario2 = Administrativo('LuLu', 1000, 8560, 'Contabilidade')
    funcionario3 = Enfermeiro('Pedro', 444, 5000, 555, 'Pediaatrico')
    funcionario4 = Medico('Maria', 555, 12000, 666, 'Cardiologica')
    
    print('\n')
    funcionario1.aumentar_salario(120)
    print('\n')
    print('Valor total: ',funcionario2.cacular_bonus())
    print('\n')
    print(funcionario3.descricao_funcao())
    print('\n')
    print(f'Salario total do {funcionario2.nome} ',funcionario2.salario_total())
    print('\n')
    
    Hospital1 = Hospital()
    Hospital1.adicionar_funcionario(funcionario1)
    Hospital1.adicionar_funcionario(funcionario2)
    Hospital1.listar_funcionarios()
    print('\n')
    print('Valor total da folha de pagamento: ', Hospital1.folha_pagamento())
    
    Hospital2 = Hospital()
    Hospital2.adicionar_funcionario(funcionario3)
    Hospital2.adicionar_funcionario(funcionario4)
    Hospital2.listar_funcionarios()
    print('\n')
    print('Valor total da folha de pagamento: ', Hospital2.folha_pagamento())
    
    
main()
