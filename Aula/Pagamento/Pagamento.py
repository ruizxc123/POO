#exemplo de polimorfismo onde o método pagar da classe Pagamento é sobrescrito nas classes filhas PagamentoPix e PagamentoCArtao
class Pagamento:
    def pagar(self, valor):
        print("Pagamento realizado! (Classe Base)")
        
        
class PagamentoPix(Pagamento):
    def pagar(self, valor):
            print("Pagamento realizado via Pix! ")


class PagamentoCartao(Pagamento):
    def pagar(self, valor):
            print("Pagamento realizado via Cartao! ")

pagamento0 = Pagamento()
pagamento1 = PagamentoPix()
pagamento2 = PagamentoCartao()

pagamento1.pagar(300)
pagamento2.pagar(20000)
pagamento0.pagar(2354)
