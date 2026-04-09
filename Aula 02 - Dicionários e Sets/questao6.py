##Você recebeu um pequeno texto e precisa analisar a frequência das palavras e identificar quais são únicas. texto = "maçã banana laranja maçã pera banana laranja laranja" Tarefas: Crie uma função chamada contar_palavras que receba o texto como string e retorne um dicionário onde: a chave é a palavra o valor é a quantidade de vezes que a palavra aparece no texto Crie uma função chamada palavras_unicas que receba o dicionário e retorne um set contendo apenas as palavras que aparecem uma única vez no texto. Imprima o dicionário de contagem e o set de palavras únicas. Dica: Para criar o set de palavras únicas, percorra o dicionário e selecione apenas as palavras cujo valor seja 1.
def contar_palavras(texto):
    lista=texto.split()
    cont = {}##dicionario vazio
    for palavra in lista:
        cont[palavra]= lista.count(palavra)
    return cont 
def palavras_unicas(dicionario):
    unicas = set()##set vazio
    for palavra, quantidade in dicionario.items():
        if quantidade == 1:
            unicas.add(palavra)    
    return unicas
dicionario = contar_palavras("maçã banana laranja maçã pera banana laranja laranja")
print(f"{contar_palavras("maçã banana laranja maçã pera banana laranja laranja")}")
palavras_unicas(dicionario)
print(f"{palavras_unicas(dicionario)}")