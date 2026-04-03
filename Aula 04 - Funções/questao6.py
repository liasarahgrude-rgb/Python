##Crie um módulo chamado calculos.py que contém duas funções: calcular_media(lista) e calcular_soma(lista). A primeira deve retornar a média dos números em uma lista e a segunda deve retornar a soma. Em outro arquivo, chamado main.py, importe as duas funções do módulo calculos.py. Crie uma lista de números [10, 20, 30, 40] e use as funções importadas para imprimir a média e a soma da lista.
def calculos(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    media = soma / len(lista) 
    return media
def soma (lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma