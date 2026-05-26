 ##Você foi convidado a desenvolver um sistema de gerenciamento de tarefas simples, utilizando Programação Orientada a Objetos (POO). Instruções: Programação Orientada a Objetos (POO): Crie uma classe chamada Tarefa com um construtor __init__ que aceite titulo e prioridade como argumentos. O construtor deve inicializar um atributo concluida como False por padrão. A classe Tarefa deve ter um método chamado marcar_concluida que muda o estado do atributo concluida para True. Crie uma instância da classe Tarefa e chame o método marcar_concluida. Comparação: No seu código principal, exiba os resultados você deve mostrar o estado da instância da tarefa antes e depois de chamar o método.
class Tarefa:
    def __init__(self, titulo, prioridade):
        self.titulo = titulo
        self.prioridade = prioridade
        self.concluida = False
        print(f"A tarefa de {self.titulo} não foi realizada!") 
    def marcar_concluida(self):
        self.concluida = True
        print(f"A tarefa de {self.titulo} foi realizada!")
tarefa1 = Tarefa("Matemática", "Média")
tarefa1.marcar_concluida()