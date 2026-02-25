from Produto import Produto

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, estoque, codigo, peso, frete):
        super().__init__(nome, preco, estoque, codigo)
        self.peso = peso
        self.frete = frete
        
    def exibir_dados(self):
        super().exibir_dados()
        print(' Peso do produto; ', self.peso)
        print(' Valor do frete: ', self.frete)
    
    def calcular_frete(self, peso):
        if peso > 0:
            self.frete = peso * 5
            return True 
        
        return False

        