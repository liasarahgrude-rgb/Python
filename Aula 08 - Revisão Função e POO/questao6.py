##Contexto: Uma empresa de eletrodomésticos precisa de um software para simular o comportamento de um termostato digital.Instruções:POO: Crie uma classe chamada Termostato com um construtor __init__ que defina um atributo chamado temperatura_atual iniciando sempre em 4 (graus Celsius).Métodos: Crie um método chamado ajustar_temperatura que receba um novo valor numérico e atualize o atributo temperatura_atual.Execução e Comparação: Instancie a classe Termostato, exiba a temperatura padrão de fábrica, altere-a usando o método criado para 2 graus e exiba o novo valor na tela para validar a alteração.
class Termostato:
    def __init__(self):
        self.temperatura_atual = 4
    def ajustar_temperatura(self,nova_temperatura):
        self.temperatura_atual = nova_temperatura

temp = Termostato()
print(f"A temperatura atual é {temp.temperatura_atual} graus Celsius")
temp.ajustar_temperatura(2)
print(f"A nova temperatura é {temp.temperatura_atual} graus Celsius")