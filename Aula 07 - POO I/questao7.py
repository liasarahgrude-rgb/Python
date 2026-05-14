##Sua tarefa é criar uma classe base ContaBancaria e uma subclasse ContaSalario. O objetivo é usar super() para garantir a correta inicialização da classe base e para estender o comportamento de um método. Crie a classe ContaBancaria com um construtor (__init__) que recebe e armazena o titular e o saldo em atributos. Adicione um método exibir_saldo que imprima o saldo atual da conta. Crie uma subclasse ContaSalario que herde de ContaBancaria. O construtor de ContaSalario deve receber o titular, o saldo e um limite_saque_diario. Ele deve usar super() para chamar o construtor de ContaBancaria, inicializando o titular e o saldo. Crie um método sacar na ContaSalario que, antes de realizar o saque, use super() para chamar o método exibir_saldo da superclasse, e depois realize o saque.
class ContaBancaria:
  def __init__(self, saldo):
    self.saldo = saldo
  def exibir_saldo(self):
    print(f"O saldo atual da conta é {self.saldo}")
class ContaSalario(ContaBancaria):
  def __init__(self, saldo,limite_saque_diario):
    super().__init__(saldo)
    self.limite_saque_diario = limite_saque_diario
  def sacar(self, valor):
    super().exibir_saldo()
    
    if valor <= self.saldo:
      self.saldo -= valor
      print(f"Saque de {valor} realizado com sucesso!")
    else:
      print(f"Saldo insuficente")
val_um = ContaBancaria(100)
val_um.exibir_saldo()
val_dois = ContaSalario(100, 10)
val_dois.sacar(50)
  