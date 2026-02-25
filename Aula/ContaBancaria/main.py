from ContaBancaria import ContaBancaria
samuel = ContaBancaria("Samuel", 111, 111, 1)
pedro = ContaBancaria("Pedro", 200, 222, 2)

nomeconta = ''

def main():
    while True:
        print('\n')
        print('-- Bem vindo     --')
        print('1- Mostra saldos --')
        print('2- Depositar     --')
        print('3- Transferir    --')
        print('4- Altera Limite --')
        print('5- Sair--')
        menu = str(input('Escolha umas das opções:  '))
        nomeConta = (input('Digite o nome da conta: ')).lower().strip()
        
        if menu == '1':
            if nomeConta == 'samuel':
                print(f'Bem vindo {nomeConta}')
                print('\n',"Saldo da sua conta Samuel:", samuel.get_saldo())
            elif nomeConta == 'pedro':
                print(f'Bem vindo {nomeConta}')
                print('\n',"Saldo da sua conta Pedro:", pedro.get_saldo())
                
            else:
                print('Conta invalida!')
                return
            
        elif menu == '2':
            if nomeConta == 'samuel':
                print(f'Bem vindo {nomeConta}')
                samuel.depositar(float(input('Digite o valor do depositor na conta Samuel:  ')))
                print('\n',"Saldo da sua conta Samuel:", samuel.get_saldo())
            elif nomeConta == 'pedro':
                print(f'Bem vindo {nomeConta}')
                pedro.depositar(float(input('Digite o valor do depositor na conta Pedro:  ')))
                print('\n',"Saldo da sua conta Pedro:", pedro.get_saldo())
            else:
                print('Conta invalida!')
                return      

            
        elif menu == '3':
            ContaTransfirir = str(input('Digite o nome da conta : '))
            valor = float(input('Digite o valor da transferencia: '))
            if nomeConta == 'samuel':
                samuel.transferir(valor,ContaTransfirir)
            elif nomeConta == 'pedro':
                pedro.transferir(valor,ContaTransfirir)
            else:
                print('Conta invalida!')
                return

            
        elif menu == '4':
            if nomeConta == 'samuel':
                valor = float(input('Digite o novo limite da conta Samuel: '))
                samuel.altera_limite(valor)
            elif nomeConta == 'pedro':
                valor = float(input('Digite o novo limite da conta Pedro: '))
                pedro.altera_limite(valor)
            else:
                print('Conta invalida!')
                return

            
                    
        '''samuel.transferir(200,pedro) 
        print("Bem vindo ao Banco  Palmas")
        
        
        print('\n',"Saldo Samuel:", samuel.get_saldo())
        print("Saldo: Pedro:", pedro.get_saldo())
        
        
        pedro.depositar(float(input('Digite o valor do depositor na conta Pedro:  ')))
        print("Saldo Pedro:", pedro.get_saldo())
        
        print('\n',samuel.depositar(574))     
        samuel .get_saldo()
        print('\n')
        pedro.altera_limite(300)
        pedro.get_limite()
        
        print('\n',pedro.exibir_dados())    
        
        
        print('\n',samuel.exibir_dados())    
        '''
        print('\n' ,pedro.exibir_historico())
        print('\n' ,samuel.exibir_historico())
        
main()
'''from ContaBancaria import ContaBancaria

def main():
    print("Bem vindo ao Banco  Palmas")
    contaSamuel = ContaBancaria("Samuel", 1000,2323, 434 )
    contaPedro = ContaBancaria("Pedro", 500, 3434, 123213)
    
    print("Saldo Samuel:", contaSamuel.get_saldo())
    print("Saldo: Pedro", contaPedro.get_saldo())
    
    contaSamuel.transferir(600, contaPedro)
    contaPedro.alterar_limite(900)
    
    print("Após transferir! ")
    print("Saldo Pedro:", contaPedro.get_saldo())
    print("Saldo Samuel:", contaSamuel.get_saldo())
    
    contaPedro.exibir_dados()
    
    contaSamuel.exibir_historico()
    
main() '''