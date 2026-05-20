class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            print(f"Erro")
computador = Produto("Notebook", 200)
print(f"Valor de custo: {computador.preco}")
computador.preco = -20