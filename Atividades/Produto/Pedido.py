from Produto import Produto

class Pedido(Produto):
    def __init__(self, nome, preco, estoque, codigo, numero, valor_total):
        super().__init__(nome, preco, estoque, codigo)
        self.numero = numero
        self.valor_total = valor_total
        self.lista_produtos = []

    def 