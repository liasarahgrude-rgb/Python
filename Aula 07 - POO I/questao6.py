##Vamos simular o comportamento de veículos. Você precisa criar uma classe base Veiculo e uma classe filha CarroEletrico. Crie a classe Veiculo com um método chamado acelerar. Este método deve imprimir a mensagem "O veículo está acelerando.". Crie uma classe CarroEletrico que herde de Veiculo. Na classe CarroEletrico, sobrescreva o método acelerar para que ele imprima uma mensagem mais específica, como "O carro elétrico está acelerando silenciosamente.". Crie uma instância de Veiculo e outra de CarroEletrico. Chame o método acelerar para cada uma e observe a diferença de comportamento.
class Veiculos:
  def __init__(self):
    pass
  def acelerar(self,acelerar):
    self.acelerar = acelerar
    print(f"O veículo está acelerando.")
class CarroEletrico(Veiculos):
  def __init__(self):
    pass
  def acelerar(self,acelerar):
    self.acelerar = acelerar
    print(f"O veículo está acelerando silenciosamente.")
carro_b = CarroEletrico()
carro_a = Veiculos()
carro_a.acelerar(True)
carro_b.acelerar(True)