##Agora, vamos aplicar todos os conceitos em um pequeno projeto: um sistema simples de gestão de contas bancárias. Você vai criar uma classe que representa uma conta e outra para gerenciar um cliente. ##Parte 1: A Classe ContaBancaria Crie uma classe chamada ContaBancaria. Ela deve ter: Um construtor __init__ que inicializa os atributos de instância numero_conta (string) e saldo (número). O saldo inicial deve ser 0. Um método depositar(valor) que adiciona o valor ao saldo. Ele deve verificar se o valor é positivo. Um método sacar(valor) que retira o valor do saldo. Ele deve verificar se o valor é positivo e se há saldo suficiente para o saque. Um método verificar_saldo() que retorna o saldo atual. 
##Parte 2: A Classe Cliente Crie uma classe chamada Cliente. Ela deve ter: Um construtor __init__ que inicializa os atributos de instância nome (string) e conta (que será um objeto da classe ContaBancaria). Parte 3: Interagindo com as Classes Crie um objeto da classe ContaBancaria com um número de conta de sua escolha. Crie um objeto da classe Cliente, passando um nome e o objeto da conta que você acabou de criar. Use o objeto do cliente para interagir com sua conta: Deposite 1000 reais. Verifique e imprima o saldo. Tente sacar 200 reais. Verifique e imprima o novo saldo. Tente sacar 900 reais para ver a validação de saldo insuficiente. Dica: No construtor da classe Cliente, você não deve criar uma nova conta, mas sim receber um objeto de ContaBancaria já existente. Isso demonstra como objetos podem conter outros objetos como atributos, uma característica poderosa da POO.
class ContaBancaria:
    def __init__(self,numero_conta):
        self.numero_conta = numero_conta ##= serve para guardar um valor e == serve para comparar se dois valores são iguais.
        self.saldo = 0
    def depositar_valor(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado!")
    def sacar(self, valor2):
        if valor2 > 0:
            if valor2 <= self.saldo:
                self.saldo -= valor2
                print(f"Saque de R${valor2} realizado!")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def verificar_saldo(self):
        return self.saldo
    
class Cliente:
    def __init__(self, meu_cliente, minha_conta):
        self.meu_cliente = meu_cliente
        self.conta = minha_conta

saldo1 = ContaBancaria(1000)
minha_conta = ContaBancaria("123-4")
meu_cliente = Cliente("João", minha_conta)

print("--- Testando Depósito ---")
meu_cliente.conta.depositar_valor(1000)

print("--- Verificando Saldo ---")
saldo_atual = meu_cliente.conta.verificar_saldo()
print(f"O saldo na tela é: {saldo_atual}")

# Testando o saque que deve funcionar
print("--- Tentando sacar R$200 ---")
meu_cliente.conta.sacar(200)
print(f"Saldo atual: {meu_cliente.conta.verificar_saldo()}")

# Testando o saque que deve falhar
print("--- Tentando sacar R$900 ---")
meu_cliente.conta.sacar(900)
print(f"Saldo atual: {meu_cliente.conta.verificar_saldo()}")