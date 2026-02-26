from Produto import Produto
from ProdutoFisico import ProdutoFisico
from ProdutoDigital import ProdutoDigital
from Pedido import Pedido


def main():
        
        Produto2 = ProdutoFisico('Tenis', 25.00, 8, 222, 10, 10)
        Produto3 = ProdutoDigital('celular', 100.00, 0, 333, 100, 'MB')
        
        Produto4 = ProdutoFisico('Camiseta', 50.00, 20, 444, 5, 5)
        Produto5 = ProdutoDigital('Calça', 80.00, 0, 555, 200, 'MB')
        
        
        Pedido1 = Pedido(1)
        Pedido1.adicionar_produtos(Produto2, 2)
        Pedido1.adicionar_produtos(Produto3, 10)
        Pedido1.exibir_resumo()
        
        Pedido2 = Pedido(2)
        Pedido2.adicionar_produtos(Produto2, 3)
        Pedido2.adicionar_produtos(Produto4, 5)
        Pedido2.adicionar_produtos(Produto5, 3)
        Pedido1.exibir_resumo()
        
        Pedido2.exibir_resumo()
        '''Produto2.exibir_dados() 
        Produto3.exibir_dados()'''
        
          
        '''if Produto2.vender_produto(5):
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
    
        Produto3.gerar_link_download()'''
main()