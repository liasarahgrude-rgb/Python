##Crie um programa em Python que gerencie uma agenda de contatos utilizando dicionários e tuplas. O programa deve: Permitir que o usuário adicione 3 contatos, onde cada contato tem nome (chave), e-mail e telefone (armazenados em uma tupla). Permitir que o usuário busque um contato pelo nome e exiba seus dados, se existir. Exibir a agenda completa após a adição. 
agenda = {}
for i in range(3):
    nome = (input("Digite seu nome: "))
    email = (input("Digite seu email: "))
    telefone = (input("Digite seu telefone: "))
    agenda[nome] = (email, telefone)
desejo = input(f"Digite o seu nome para fazermos a verificação: ")
if desejo in agenda:
    email, telefone = agenda[desejo]
    print(f"As informações de email e telefone de {desejo} são {email, telefone}") 
else :
    print(f"Informações invalidas, a pessoa não foi cadastrada no sistema!")
    
for nomes, dados in agenda.items():
    email1, telefone1 = dados
    print(f"Nome: {nomes} | E-mail: {email1} | Telefone: {telefone1}")