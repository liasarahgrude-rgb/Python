##Crie uma função que recebe uma lista de números e retorna uma nova lista apenas com os números pares, usando uma função normal e depois usando uma função lambda com filter. Exemplo de lista de números: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
def lista(nums):
    vazia = []
    for par in nums:
        if par % 2 == 0:
            vazia.append(par)
    return vazia 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vazia2 = lista(numeros)
print(f"Os números pares da lista são {vazia2}")