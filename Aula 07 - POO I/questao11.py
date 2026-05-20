##Um Carro tem um Motor que é uma parte inseparável dele (composição). O Motor tem uma potência que precisa ser validada para nunca ser um valor negativo (encapsulamento). Instruções: Crie a classe Motor com o atributo privado __potencia. Use o @property para permitir a leitura e o setter para validar se a potência é maior que zero. Crie a classe Carro com o atributo marca. No construtor, crie uma instância de Motor dentro do Carro (composição). Crie uma instância de Carro. Tente exibir a potência do motor e, depois, tente alterá-la para um valor válido e um inválido para testar a validação.
class Motor:
    def __init__(self, potencia):
        self.__potencia = potencia
    @property
    def potencia(self):
        return self.__potencia
    @potencia.setter
    def potencia(self, potencia):
        if potencia > 0:
            self.__potencia = potencia
        else:
            print(f"Invalido")
class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor(120)
carro1 = Carro("Byd")
carro1.motor.potencia = -90
print(carro1.motor.potencia)
