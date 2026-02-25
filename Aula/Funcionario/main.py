from Funcionario import Funcionario
from Gerente import Gerente
from Estagiario import Estagiaro


def main():
    Funcionario1 = Funcionario('Marta', 5623)
    Funcionario2 = Gerente('Pedro', 12000, 'Gerência')
    Funcionario3 = Estagiaro('Rui', 1600)
    
    Funcionario1.exibir_dados()
    Funcionario2.exibir_dados()
    Funcionario3.exibir_dados()
    
    Funcionario3.renovar_contrato()

main()
    
    