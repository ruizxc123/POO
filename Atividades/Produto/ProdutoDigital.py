from Produto import Produto

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, estoque, codigo, tamanho_arquivo, formato):
        super().__init__(nome, preco, estoque, codigo)
        self.tamanho_arquivo = tamanho_arquivo
        self.formato = formato
        
    def vender_produto(self, qtd):
        print(f'\nProduto digital vendido! Nome do produto {self.nome}')   
    
    def exibir_dados(self):
        super().exibir_dados()
        print(' Tamanho do arquivo: ', self.tamanho_arquivo)
        print(' Tipo de arquivo: ', self.formato)
        
      
    def gerar_link_download(self):
        print('\n Link de download enviado para o cliente')  
        
    