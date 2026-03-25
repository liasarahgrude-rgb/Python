estoque = {"mouse": 20, "teclado": 15} 
estoque["mouse"] = 10
estoque["monitor"] = 8 
del estoque["teclado"] 
print(estoque)

contato = {"nome": "Carlos"} 
chaves = ["nome", "idade"]
contato["idade"] = 30 
if "idade" in contato and "nome" in contato:
    print("Dados completos")
else: print("Faltam dados")

alunos = {"Ana": 9, "Bruno": 7} 
print("Ana" in alunos)

dados = {"nome": "Pedro", "idade": 22}
print(dados.get("curso", "Não encontrado"))##get comando em python p acessar a chave de um dicionario

alunos = {"Ana": 9.5, "Bruno": 6.0, "Carla": 8.0} 
aprovados = {}
for nome, nota in alunos.items():
    if nota >= 7.0: aprovados[nome] = nota 
    print(list(aprovados.keys()))##com o list na frente de aprovados, aparece só as chaves sem o dict keys

set1 = {1, 2, 3} 
set2 = {3, 4, 5} 
print(set1.union(set2))

carro = {"marca": "Fiat", "ano": 2020, "cor": "preto"}
print (carro.keys())##sem o list na frente do carro o que sai no terminal é dict_keys


pessoa = {"nome": "Maria", "idade": 25}
print(pessoa)
pessoa ['idade'] = 26
print(pessoa)


dados = {"nome": "Paula", "idade": 23}


print(dados['idade'])
print(dados['nome'])
print(dados.get('profissao'))

carrinho = {"blusa": 50, "calça": 100, "sapato": 150}
total = sum(carrinho.values())
print(total)

numeros = [5, 2, 8, 2, 5, 1] 
conjunto = set(numeros)##Quando você faz conjunto = set(numeros), o Python converte a lista em um conjunto.
print(len(conjunto))##A função len(conjunto) conta quantos itens restaram após a limpeza das duplicatas.

vendas = {"jan": 150, "fev": 200, "mar": 120}
total_anual = 0
for mes, valor in vendas.items(): 
    total_anual += valor 
print(total_anual)