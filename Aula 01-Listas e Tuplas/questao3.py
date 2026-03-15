##Crie um programa que armazene uma tupla de frutas disponíveis em uma feira. O programa deve: Criar uma tupla com pelo menos 5 frutas. Exibir todas as frutas disponíveis. Perguntar ao usuário o nome de uma fruta e informar se ela está disponível ou não na feira. Exibir a quantidade total de frutas na tupla.
frutas = ("maça", "banana", "uva", "abacate")##Para criar uma tupla tem que colocar a virgula
print(f"As frutas disponíveis são : {frutas}")
fruta = input("Digite o nome da fruta desejada: ")
if fruta in frutas: 
    print("A fruta desejada está disponível!")
else:
    print("A fruta desejada está indisponível!")
print(f"Temos {len(frutas)} frutas disponíveis!")##A função len() em Python retorna o número total de elementos (itens) contidos em uma tupla