##Sua tarefa é desenvolver um pequeno sistema de processamento de pedidos que lide com diferentes tipos de produtos, utilizando herança, sobrescrita, super() e polimorfismo. Crie uma classe base chamada Pedido. O construtor deve receber um nome_produto e um preco. Adicione um método processar_envio que imprima "Enviando pedido de produto genérico.". Crie duas subclasses de Pedido: PedidoEletronico e PedidoRoupa. Sobrescreva o método processar_envio em ambas as subclasses com mensagens mais específicas. Em PedidoEletronico, a mensagem deve ser print(f"Adicionando seguro e número de série {self.serial_number} ao pacote."). Em PedidoRoupa, a mensagem deve ser print(f"Adicionando embalagem especial para vestuário. Tamanho - {self.tamanho}"). Em ambas as subclasses, o construtor (__init__) deve usar super() para inicializar os atributos da classe base. 
# Crie uma lista com instâncias de PedidoEletronico e PedidoRoupa. Use um loop for para iterar sobre a lista de pedidos e chame o método processar_envio para cada ite Isso demonstrará o polimorfismo, onde a mesma chamada de método tem comportamentos diferentes.m.
##O polimorfismo, que significa "muitas formas", é um princípio da POO que permite que objetos de diferentes classes respondam ao mesmo chamado de método de maneiras distintas, desde que essas classes compartilhem uma interface comum (geralmente através de herança)

class Pedido:
    def __init__(self, nome_produto, preco):
        self.nome_produto = nome_produto
        self.preco = preco
    def processar_envio(self):
        print(f"Enviando pedido de produto genérico.")
class PedidoEletronico(Pedido):
    def __init__(self, nome_produto, preco, serial_number):
        super().__init__(nome_produto, preco)
        self.serial_number = serial_number
        print(f"Adicionando seguro e número de série {self.serial_number} ao pacote.")
class PedidoRoupa(Pedido):
    def __init__(self, nome_produto, preco, tamanho):
        super().__init__(nome_produto, preco)
        self.tamanho = tamanho
        print(f"Adicionando embalagem especial para vestuário. Tamanho - {self.tamanho}")
lista_de_pedidos = [##"Atenção, isso aqui é uma Classe (um molde), e você está gerando um objeto a partir dela."
    PedidoEletronico("Smartphone", 2500.00, "SN-987654"),
    PedidoRoupa("Camiseta Básica", 79.90, "G"),
    PedidoEletronico("Notebook", 4500.00, "SN-123456"),
    PedidoRoupa("Calça Jeans", 149.00, "42")
]
##Na primeira volta, a variável pedido passa a apontar para o primeiro objeto da lista (o Smartphone). Quando o código executa pedido.processar_envio(), o Python não olha para a lista. Ele olha para o objeto que está na variável pedido e pergunta para ele: "De qual classe você nasceu?"O objeto responde: "Eu nasci da classe PedidoEletronico".
for Pedido in lista_de_pedidos:
    Pedido.processar_envio