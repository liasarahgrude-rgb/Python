##Crie uma função chamada calcular_imovel que aceita os parâmetros area, tipo_imovel (com valor padrão 'apartamento') e tipo_negocio (com valor padrão 'venda'). A função deve imprimir uma frase descrevendo a transação. Chame a função de três maneiras diferentes: Usando apenas argumentos posicionais. Usando argumentos nomeados para tipo_negocio e tipo_imovel. Usando uma combinação de argumentos posicionais e nomeados, alterando apenas o tipo_imovel.
def calcular_imovel (area, tipo_imovel = "apartamento" , tipo_negocio = "venda"):
    print(f"Transação da area {area}, do {tipo_imovel}, por {tipo_negocio}")
calcular_imovel(20, "casa", "aluguel")##Argumentos posicionais
calcular_imovel(20 ,tipo_imovel = "casa", tipo_negocio = "aluguel")##Argumentos posicionais
calcular_imovel(20,"triplex", tipo_negocio= "aluguel")

def calcular_imovel (area, tipo_imovel = "apartamento" , tipo_negocio = "venda"):
    print(f"Transação da area {area}, do {tipo_imovel}, por {tipo_negocio}")
calcular_imovel(20, "casa", "aluguel")##Argumentos posicionais
calcular_imovel(20 ,tipo_imovel = "casa", tipo_negocio = "aluguel")##Argumentos posicionais
calcular_imovel(20,"triplex", tipo_negocio= "aluguel")