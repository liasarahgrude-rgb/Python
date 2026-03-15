##Crie um programa que gerencie uma lista de compras. O programa deve: Perguntar ao usuário quantos itens deseja adicionar. Utilizar um for para ler cada item e armazená-lo em uma lista. Após o cadastro, exibir a lista completa de compras. Perguntar ao usuário se deseja remover algum item. Se o usuário informar um item existente, remova-o da lista e exiba a lista atualizada.
lista = []##Inicializa a lista vazia
itens = int (input("Quantos itens você deseja adicionar? "))
for itens2 in range(0, itens):##vai percorrer de 0 ate o valor digitado pelo usuario e armazenado em "itens"
    nome = input("Qual nome do item? ")
    lista.append(nome)##Append é o comando responsavél por add os elementos na lista que inicializamos vazia e agora tem o nome do item
remover = int(input("Você deseja remover algum item?\nDigite 0 para sim e 1 para não: "))
while remover == 0:##Vai repetir a pergunta enquanto a pessoa quiser remover algo da lista
    remover2 = input("Qual elemento da lista você quer retirar? ")
    if remover2 in lista:##Verifica se o remover2(a string que a pessoa digitou) está na lista
        lista.remove(remover2)##.remove é o comando responsável por remover elementos da lista 
        print(f"Sua lista atualizada é: {lista}")
    elif remover2 not in lista:
         print(f"Esse item não está na lista ou você digitou mais de um produto!")
    remover = int(input("Você deseja remover algum item?\nDigite 0 para sim e 1 para não: "))
if remover == 1:
        print(f"Sua lista é: {lista}")