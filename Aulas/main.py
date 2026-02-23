from ContaBancaria import ContaBancaria

def main():
    print("Bem vindo ao Banco  Palmas")
    contaSamuel = ContaBancaria("Samuel", 111, 111, 1,[])
    contaPedro = ContaBancaria("Pedro", 200, 222, 2,[])
    
    print('\n',"Saldo Samuel:", contaSamuel.get_saldo())
    print('\n',"Saldo: Pedro", contaPedro.get_saldo())
    
    contaPedro.depositar(349)
    print("Saldo Pedro:", contaPedro.get_saldo())
    
    print('\n',contaSamuel.depositar(574))     
    contaSamuel.get_saldo()
    print('\n')
    contaPedro.altera_limite(300)
    contaPedro.get_limite()
    
    print('\n',contaPedro.exibir_dados())
    
    contaPedro.transferir(200,contaSamuel)
    
    print('\n',contaSamuel.exibir_dados())    
    
    print('\n' ,contaPedro.exibir_historico())
    print('\n' ,contaSamuel.exibir_historico())
    
main()