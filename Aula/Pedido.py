class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.valor_total = 0
        self.lista_produtos = []

    def adicionar_produtos(self, produto, qtd):
        self.lista_produtos.append((produto, qtd))    
        produto.vender_produto(qtd)
        
    def calcular_total(self):
        total_parcial = 0
        for produto, qtd in self.lista_produtos:
            total_parcial += produto.preco * qtd
        self.valor_total = total_parcial
        return self.valor_total
    
    def exibir_resumo(self):
        print('-----Resumo----- ')
        for produto, qtd in self.lista_produtos:
            print(f'--{produto.nome} -- quantidade {qtd}')
        print('Total: R$ ', self.calcular_total())
        
