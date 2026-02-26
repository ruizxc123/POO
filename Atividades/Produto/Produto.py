class Produto:
    def __init__(self, nome, preco, estoque, codigo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.codigo = codigo
        
    def exibir_dados(self):
        print('\n nome:', self.nome)
        print(' Preço R$: ', self.preco)
        print(' Estoque do produto: ', self.estoque)
        print(' Codigo do produto: ', self.codigo)
    
    
    def atualizar_preco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
            
            return True
        
        return False
    
    
    def adicionar_estoque(self, qtd):
        if qtd > 0:
            self.estoque += qtd  
            return True
        
        return False
    
    
    def vender_produto(self, qtd):
        if self.estoque >= qtd:
            self.estoque -= qtd

            return True
        
        return False
            