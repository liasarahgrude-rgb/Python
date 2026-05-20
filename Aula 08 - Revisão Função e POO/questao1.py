#Sua tarefa é criar três funções em Python que interagem entre si para realizar os cálculos. Instruções: Crie uma função chamada calcular_total_pedido que aceita um parâmetro chamado itens_pedido. Esse parâmetro será um dicionário onde as chaves são os nomes dos itens e os valores são os preços. A função deve retornar a soma total dos preços. Crie uma segunda função chamada aplicar_desconto que aceita dois parâmetros: o total do pedido (o valor retornado pela primeira função) e a porcentagem do desconto. A função deve calcular o valor com desconto e retorná-lo. Se a porcentagem de desconto for 0, retorne o total sem alteração. Crie uma terceira função chamada resumo_pedido que aceita o total_final (o valor após o desconto) e um parâmetro opcional chamado taxa_servico com um valor padrão de 0.10 (10%). A função deve calcular o valor final com a taxa de serviço e exibir um resumo do pedido, mostrando o valor original, o valor com desconto e o valor final com a taxa. A função não deve retornar nada (use apenas print). No corpo principal do seu script, defina um dicionário com alguns itens e preços. Chame as funções na ordem correta, passando os valores e armazenando os retornos em variáveis para uso posterior. Passe o valor 15.00 como porcentagem de desconto. Dica: Lembre-se de que a função resumo_pedido pode ser chamada sem o argumento taxa_servico, e nesse caso o valor padrão deve ser usado.
itens_pedido = {
        "Cafe":12, "Tapioca":15, "Pão com ovo":20
    }
def calcular_total_pedido(itens_pedido):
    total = sum(itens_pedido.values())
    return total
def aplicar_desconto(total, porcentagem):
    if porcentagem > 0:
        desconto = total * (porcentagem/100)
        val_desconto = total - desconto 
        return val_desconto
    return total
def resumo_pedido(total, val_desconto,taxa_servico=0.10):
    taxa_ser = val_desconto * taxa_servico 
    conta_total = val_desconto + taxa_ser
    print(f"A sua conta com a taxa de serviço ficou: ${total}")
    print(f"A sua conta com a taxa de serviço ficou: ${conta_total}")
    print(f"A sua conta sem a taxa de serviço ficou: ${val_desconto}")


total_bruto = calcular_total_pedido(itens_pedido)
print(total_bruto)

total_liquido = aplicar_desconto(total_bruto, 15)
print(total_liquido)
resumo_pedido(total_bruto, total_liquido)
    