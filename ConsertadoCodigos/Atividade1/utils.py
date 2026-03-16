


def calcular_desconto(preco, porcentagem): 
    desconto = preco * (porcentagem / 100) 
    return preco - desconto 

def exibir_produto(produto): 
    print("Produto:", produto.nome) 
    print("Preço:", produto.preco) 