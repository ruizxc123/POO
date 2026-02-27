from abc import ABC, abstractmethod
import math

class Forma(ABC):  # Classe abstrata
    def __init__(self, cor):
        self.cor = cor
        
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass
    
    def exibir_cor(self):
        print("Cor da forma: ", self.cor)
    
    
class Retangulo(Forma):
    def __init__(self, largura, altura, cor):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
        
class Circulo(Forma):
    def __init__(self, raio, cor):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self):
        return 3.14 * pow(self.raio, 2)

    def calcular_perimetro(self):
        return 2*math.pi*self.raio
        
forma1 = Retangulo(5, 9, 'roxo')
forma2 = Circulo(5, 'amarelo')

print(forma1.calcular_perimetro())
print(forma2.calcular_perimetro())

forma1.exibir_cor()
forma2.exibir_cor()
'''
#exemplo de abstração

#ABC -> Para dizer que uma classe é abstrata(não é possível criar instância dela)
#abstractmethod -> Para dizer que um método é abstrato, ou seja obriga as subclasses o implementarem
from abc import ABC, abstractmethod 

class Forma(ABC):  # classe abstrata(não é possível criar instância dela)
    def __init__(self, cor):
        self.cor = cor
    
    @abstractmethod
    def calcular_area(self): #metodo abstrato, obriga subclasses implementarem ele
        pass
    
    def exibir_cor(self): #método comum, não é obrigatório sobrescrever nas subclasses
        print("Cor: ", self.cor)


class Retangulo(Forma): #subclasse da classe Forma
    def __init__(self, largura, altura, cor):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura

    #método obrigatório de ser implementado pois a superclasse(Forma) diz que ele é abstrato
    def calcular_area(self): 
        return self.largura * self.altura
    

class Circulo(Forma):#subclasse da classe Forma
    def __init__(self, raio, cor):
        super().__init__(cor)
        self.raio = raio

    #método obrigatório de ser implementado pois a superclasse(Forma) diz que ele é abstrato
    def calcular_area(self):
        return 3.14 * pow(self.raio, 2)

#instâncias
forma1 = Retangulo(5, 9, 'verde')
forma2 = Circulo(6, 'amarelo')

#acessando métodos
print(forma1.calcular_area())
print(forma2.calcular_area())

'''