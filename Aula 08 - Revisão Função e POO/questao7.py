##Contexto: Você está desenvolvendo o esqueleto do sistema de transações de um banco digital.Instruções:POO e Encapsulamento: Crie uma classe chamada ContaBancaria. O construtor deve aceitar o nome do titular e iniciar um atributo privado (ou protegido) chamado _saldo com o valor de 0.0.Métodos: - Crie um método chamado depositar que receba um valor e o some ao _saldo.Crie um método chamado sacar que receba um valor. Este método deve verificar se o saldo é suficiente. Se for, subtraia o valor; se não for, exiba uma mensagem de "Saldo Insuficiente".Execução e Comparação: Instancie a conta, realize um depósito de 100.0 reais e exiba o saldo (via método ou propriedade de leitura). Em seguida, tente fazer um saque de 150.0 reais (mostrando o aviso de erro) e, logo depois, um saque de 40.0 reais, exibindo o saldo final restante.
class ContaBancaria:
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
        self._saldo = 0.0##Variavel privada
    
    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
        else:
            print(f"Saldo insuficiente para saque")
        
    def get_saldo(self):##Função para exibir a variavel privada
        return self._saldo

conta = ContaBancaria("João")
conta.depositar(100.0)
conta.sacar(150.0)
conta.sacar(40.0)
print(f"Saldo final: R${conta.get_saldo():.2f}")