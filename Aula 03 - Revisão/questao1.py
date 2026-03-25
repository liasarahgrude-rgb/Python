##Você recebeu a lista de notas notas_brutas = [8.5, 9.0, 7.5, 8.0, 6.5, 9.0, 10.0, 5.0, 8.5]. Escreva um código que use um laço for para calcular a média de todas as notas. Use uma list comprehension para criar uma nova lista chamada notas_aprovados contendo apenas as notas que são maiores ou iguais a 7.0. Imprima a média e a lista de notas dos aprovados.
notas_brutas = [8.5, 9.0, 7.5, 8.0, 6.5, 9.0, 10.0, 5.0, 8.5]
nota = 0
for estagiario in notas_brutas:
    nota += estagiario 
media = nota / len (notas_brutas)
notas_aprovados = [n for n in notas_brutas if n >= 7 ]
print (f"A média dos alunos é: {media}")
print(f"A lista de nota dos aprovados é: {notas_aprovados}")