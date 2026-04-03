##Crie uma função cadastro que receba nome, idade e cidade usando **kwargs, e exiba cada dado.
def coletar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f" {chave} - {valor}")
nome = input("Digite o seu nome: ")
idade = input ("Digite sua idade: ")
cidade = input (("Digite sua cidade: "))
coletar_dados(nome={nome}, idade={idade}, cidade={cidade})