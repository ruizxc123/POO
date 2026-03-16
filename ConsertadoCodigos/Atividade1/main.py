from models.Produto import Produto
from utils import calcular_desconto, exibir_produto

def main(): 
    
    p1 = Produto("Notebook", 3500) 
    p2 = Produto("Mouse", 120) 
    
    exibir_produto(p1) 
    
    novo_preco = calcular_desconto(p1.preco, 10) 
    
    print("Preço com desconto:", novo_preco) 
    print() 
    
    exibir_produto(p2) 
    novo_preco = calcular_desconto(p2.preco, 5) 
    print("Preço com desconto:", novo_preco) 
    
main() 

