from abc import ABC, abstractmethod

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
            self.salario = self.salario * porcetagem_salario        
            return True
        
    def salario_total(self):
        return self.salario + self.cacular_bonus()
    
    def exibir_dados(self):
        print('\n----Dados-----')
        print("Nome: ", self.nome)
        print("Registro: ", self.resgistro)
        print("Salário: ", self.salario)
    
    def desativar(self, demitir):
        if self.ativo == True :
            self.ativo = demitir
            return True
        else:
            return False
