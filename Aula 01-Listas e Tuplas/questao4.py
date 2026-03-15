##Projeto Final - Sistema de Cadastro de Alunos Objetivo Desenvolva um programa que cadastre 3 alunos, colete suas notas e apresente um relatório final com a situação de cada um. Funcionalidades esperadas: 1. Cadastro de dados Solicite o nome de 3 alunos Para cada aluno, peça sua nota (0 a 10) Armazene os dados em listas separadas 2. Processamento Para cada nota, determine a situação: Nota ≥ 7: "Aprovado" Nota ≥ 5 e < 7: "Recuperação" Nota < 5: "Reprovado" 3. Relatório final Exiba uma tabela organizada com: Nome do aluno Nota obtida Situação acadêmica Exemplo de saída esperada: Nome Nota Situação ----------------------------- Maria 9.0 Aprovado Renato 6.0 Recuperação Alan 3.0 Reprovado onceitos que você deve aplicar: Listas para armazenar nomes e notas Loop for com range() para coletar dados Estruturas condicionais para classificar situações Formatação de saída com espaçamento adequado
nome = []##Inicaliza a lista vazia para armazenar o nome dos alunos
notas = []
print(f"---Cadastro de alunos---")
for alunos in range(3):##For vai percorrer do 0 até o valor 3
    nomeAL = input("Digite o nome do aluno: ")
    nome.append(nomeAL)##.append adiciona o nome dos alunos na lista "nome"

for avaliacoes in range(3):##Mesmo raciocinio do for anterior
    notasep = float(input(f"Digite a nota do aluno {avaliacoes+1} : "))
    notas.append(notasep)

for i in range(3):##i incializa em 0,1,2 e percorre a lista de notas
    if notas[i] >= 7:
        print(f"Aluna (o) {nome[i]} nota: {notas[i]} situação: Aprovada(o)!")
    elif notas[i] >= 5 and notas[i] < 7:
        print(f"Aluna (o) {nome[i]} nota: {notas[i]} situação: Recuperação!")
    elif notas[i] < 5:
        print(f"Aluna (o) {nome[i]} nota: {notas[i]} situação: Reprovada(o)!")