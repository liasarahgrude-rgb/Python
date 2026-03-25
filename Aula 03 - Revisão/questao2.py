##Você recebeu a lista de registros de notas registros = [("João", 8.5), ("Maria", 9.0), ("Pedro", 7.5)]. Escreva um código que use um laço for com desempacotamento de tupla para calcular a média de todas as notas. Imprima o nome do aluno com a maior nota.
notas_registros = [("João", 8.5), ("Maria", 9.0), ("Pedro", 7.5)]
nota = 0
for alunos, notas in notas_registros: 
    nota += notas
media = nota / len (notas_registros)
print (f"{media:.2f}")
maior = 0
nome = ""
for nomes, notas in notas_registros:
    if notas > maior:
        maior = notas
        nome = nomes
print(f"O aluno com a melhor nota é {nome} e sua nota é {maior}")