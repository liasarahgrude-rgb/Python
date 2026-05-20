##Em um sistema, uma Loja pode ter vários Vendedores. Cada Vendedor pode trabalhar em uma Loja e ser transferido para outra. Isso significa que a vida do vendedor não depende da loja. Instruções: Crie uma classe Vendedor com um atributo nome. Crie uma classe Loja com um atributo nome_loja e uma lista vazia chamada vendedores. Na classe Loja, crie um método contratar(vendedor) que adiciona um objeto Vendedor à lista. Crie uma instância de Vendedor e uma de Loja. Contrate o vendedor para a loja usando o método que você criou. Mostre que o vendedor existe mesmo sem a loja.
class Vendedor:
    def __init__(self, nome):
        self.nome = nome
class Loja:
    def __init__(self, nome_loja):
        self.nome_loja = nome_loja
        self.vendedores = [Vendedor("Sarah")]
    def contratar(self, vendedor):
        self.vendedores.append(vendedor)
vend1 = Vendedor("Lia")
loj2 = Loja("Romanel")
loj2.contratar(vend1)
for vendedor in loj2.vendedores:
    print(vendedor.nome)