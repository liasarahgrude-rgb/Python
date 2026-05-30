##Contexto: O setor de Recursos Humanos de uma startup precisa calcular a folha de pagamento de diferentes tipos de prestadores de serviço.Instruções:Herança: Crie uma classe base chamada Prestador. O construtor deve receber o nome do profissional. Essa classe deve ter um método chamado calcular_ganhos que retorna 0.0.Polimorfismo:Crie uma subclasse chamada Diarista que herda de Prestador. Seu construtor deve receber o nome, a quantidade_dias trabalhados e o valor_dia. Reescreva (override) o método calcular_ganhos para retornar a multiplicação dos dias pelo valor do dia.Crie outra subclasse chamada Mensalista que herda de Prestador. Seu construtor deve receber o nome e o salario_fixo. Reescreva o método calcular_ganhos para retornar o valor do salário fixo.Execução e Comparação: No código principal, crie uma lista contendo um objeto Diarista (ex: 5 dias a R$ 200/dia) e um objeto Mensalista (ex: R$ 4500 fixo). Percorra essa lista usando um loop for e, de forma polimórfica, chame o método calcular_ganhos de cada um, exibindo o nome do profissional e o valor final que ele deve receber.
class Prestador:
    def _init_(self, nome):
        self.nome = nome
        self.calcular_ganhos = 0.0

class Diarista(Prestador):
    def _init_(self, nome, quantidade_dias, valor_dia):
        super()._init_(nome)
        self.quantidade_dias = quantidade_dias
        self.valor_dia = valor_dia
        self.calcular_ganhos = self.quantidade_dias * self.valor_dia
        print(f"A {self.nome} vai ganhar {self.calcular_ganhos} por {self.quantidade_dias} dias trabalhados ")

class Mensalista(Prestador):
    def _init_(self, nome, salario_fixo):
        super()._init_(nome)
        self.salario_fixo = salario_fixo
        self.calcular_ganhos = self.salario_fixo
        print(f"A {self.nome} vai ganhar um salário fixo de {self.calcular_ganhos} pelos dias trabalhados ")

pessoa1 = Diarista("Lia", 5, 200)
pessoa2 = Mensalista("Sarah", 4500)