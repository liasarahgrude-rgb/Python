##Vamos começar descobrindo quanto vale uma moeda em relação a outra! Crie um arquivo chamado etapa1.py. Importe o módulo requests. Crie uma função chamada buscar_cotacao(moeda_base, moeda_destino). Ela deve acessar a AwesomeAPI (https://economia.awesomeapi.com.br/json/last/ ) e devolver o valor atual da cotação. Exiba o valor no terminal com print(). Dica: o formato da URL é assim: https://economia.awesomeapi.com.br/json/last/USD-BRL
import requests

def buscar_cotacao(moeda_base, moeda_destino):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}"
    resposta = requests.get(url)##Pega os resultados da API
    dados = resposta.json()##Converte em dicionario
    chave = moeda_base + moeda_destino##
    cotacao = float(dados[chave]['bid'])##
    return cotacao

valor = buscar_cotacao('USD', 'BRL')
print(f"Cotação atual USD/BRL: {valor:.2f}")
##Agora que já conseguimos buscar a cotação, vamos converter valores! Crie uma nova função chamada converter(valor, cotacao). Ela deve multiplicar o valor pela cotação e devolver o resultado. Peça ao usuário um valor e exiba o resultado da conversão.
def converter(valor, cotacao):
    return valor * cotacao
cotacao = buscar_cotacao('USD', 'BRL')
valor = 10
resultado = converter(valor, cotacao)
print(f"{resultado}")
##Vamos guardar as conversões feitas! Crie uma função registrar_historico(moeda, valor, resultado). Ela deve adicionar essas informações a uma lista chamada historico. Ao final, mostre todas as conversões já feitas.

##Vamos guardar as conversões feitas! Crie uma função registrar_historico(moeda, valor, resultado). Ela deve adicionar essas informações a uma lista chamada historico. Ao final, mostre todas as conversões já feitas.