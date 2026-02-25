from Produto import Produto
from ProdutoFisico import ProdutoFisico
from ProdutoDigital import ProdutoDigital

def main():
        Produto1 = Produto('Camisa', 50.00, 5, 111)
        Produto2 = ProdutoFisico('Tenis', 25.00, 8, 222, 10, 10)
        Produto3 = ProdutoDigital('celular', 100.00, 5, 333, 100, 'MB')
    
        Produto1.exibir_dados()
        Produto2.exibir_dados() 
        Produto3.exibir_dados()
    
        if Produto1.vender_produto(2):
            print(f'\nEstoque atualizado do produto: {Produto1.estoque} Nome do produto {Produto1.nome}')
        else:
            print('Valor invalido')
            
        if Produto2.vender_produto(-3):
            print(f'\nEstoque atualizado do produto: {Produto2.estoque} Nome do produto {Produto2.nome}')
        else:
            print('Valor invalido')

        if Produto3.atualizar_preco(125.00):
            print(f'\nPreço atualizado do produto: {Produto3.preco:.2f} Nome do produto {Produto3.nome}')
        else:
            print('Valor invalido')
        
        if Produto2.adicionar_estoque(10):
            print(f'\nEstoque atualizado do produto: {Produto2.estoque} Nome do produto {Produto2.nome}')
        else:
            print('Valor invalido')

        if Produto2.calcular_frete(Produto2.peso):
            print(f'\nValor do frete atualizado: {Produto2.frete:.2f} Nome do produto {Produto2.nome}')
        else:
            print('Valor invalido')
    
        Produto3.gerar_link_download()
main()