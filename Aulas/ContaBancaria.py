class ContaBancaria:
    def __init__(self, titular:str, saldo: float, agencia, numero_conta: int):
        self.titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.__numero_conta = numero_conta
        self.__limite = 500
        self.__historico = []
        

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite
    
    def get_agencia(self):
        return self.__agencia
    
    def get_numero_conta(self):
        return self.__numero_conta
    
    def get_historico(self):
        return self.__historico


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.append(f'Depósito : R${valor:.2f}')    
            print(f"O valor de {valor:.2f} foi depositado na conta!")
            return True
        else:
            print("Valor inválido!")
            return False
            

    def sacar(self, valor):
        if ((self.__saldo + self.__limite ) or ((self.__saldo - self.__limite) >= 0))  <= valor:
            self.__saldo -= valor
            self.__historico.append(f'Saque : R${valor:.2f}')
            return True
        else:   
            return False
    
    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor) == False:
            print("Saldo insuficiente para transferência!")
            return False
        else:
            conta_destino.depositar(valor)
            self.__historico.append(f'Transferência de R$ : {valor:.2f} para {conta_destino.titular}')
            print(f"Transferência de {valor:.2f} realizada com sucesso!")
            return True
        
        
        
    def exibir_dados(self):
        print('Nome do titular : ', self.titular)
        print('Agência : ', self.__agencia)
        print('Número da conta : ', self.__numero_conta)
        print('Saldo : ', self.__saldo)
        print('Limite : ', self.__limite)
    
    def altera_limite(self, novo_limite):
        if novo_limite <=0:
            print('Erro')
            return False
        else:
            self.__limite = novo_limite
            self.__historico.append(f'Alteração de limite para R$ : {novo_limite:.2f}')
            print('Sucesso',novo_limite)
            
    def exibir_historico(self):
        print("\n=== HISTÓRICO DE OPERAÇÕES ===")
        if self.__historico:
            for i, operacao in enumerate(self.__historico, 1):
                print(f"{i}. {operacao}")
        else:
            print("Nenhuma operação realizada ainda.")
        print("================================")