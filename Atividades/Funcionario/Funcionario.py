from abc import ABC, abstractmethod
import math

class Funcionario(ABC):
    
    def __init__(self, nome, registro, salario):
        self.nome = nome
        self.resgistro = registro
        self.salario = salario
        self.ativo = True
        
    @abstractmethod
    def cacular_bonus(self):
        pass
      
    @abstractmethod
    def descricao_funcao(self):
        pass
    
    def aumentar_salario(self, porcetagem_salario):
        if porcetagem_salario <= 0 and self.ativo == False:
            return False
        else:
            self.salario = (self.salario * (porcetagem_salario/100)) + self.salario
            return True
        
    def salario_total(self):
        return self.salario + self.cacular_bonus()
    
    def exibir_dados(self):
        print('\n----Dados-----')
        print("Nome: ", self.nome)
        print("Registro: ", self.resgistro)
        print("Salário: ", self.salario)
        print("Status: ", "Ativo" if self.ativo else "Inativo")
    
    def desativar(self):
        if self.ativo:
            self.ativo = False
            print(f'Funcionário {self.nome} desativado.')
            return True
        else:
            print(f'Funcionário {self.nome} já está inativo!.')
            return False
