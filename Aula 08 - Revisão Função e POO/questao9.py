##Contexto: Você foi designado para codificar o motor de regras de um carrinho de compras de um e-commerce.Instruções:Composição: Crie uma classe Item que receba nome e preco no construtor. Depois, crie uma classe Carrinho que inicialize uma lista vazia no construtor para armazenar os itens encomendados.Métodos e Protocolos: - Na classe Carrinho, adicione o método adicionar_item que recebe um objeto do tipo Item e o insere na lista.Implemente o método mágico __len__ na classe Carrinho para que ele retorne a quantidade de itens salvos na lista interna.Adicione um método comum chamado calcular_total que varre a lista e soma o preço de cada item.Execução e Comparação: Crie três instâncias de Item com preços diferentes. Instancie o Carrinho. Antes de adicionar qualquer item, exiba a quantidade usando a função nativa len(seu_carrinho). Adicione os itens, exiba novamente o resultado de len(seu_carrinho) para provar o funcionamento do método mágico e, por fim, exiba o valor total da compra gerado pelo calcular_total.
class Item:
    def _init_(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def _init_(self):
        self.itens_encomendados = []
    def adicionar_item(self, item):
        self.item = item
        self.itens_encomendados.append(item)##Adiciona os elementos a lista
    def _len_(self):
        return len(self.itens_encomendados)#Conta quantos elementos estão n
    def calcular_total(self):
        total = 0
        for item in self.itens_encomendados:
            total += item.preco
        return total

item1 = Item("Bola", 100)
item2 = Item("Barbie", 80)
item3 = Item("Escova", 150)
carrinho = Carrinho()

carrinho.adicionar_item(item1)
carrinho.adicionar_item(item2)
carrinho.adicionar_item(item3)

print(f"No seu carrinho tem {len(carrinho)} itens")
print(f"O valor total do seu carrinho é {carrinho.calcular_total()}")