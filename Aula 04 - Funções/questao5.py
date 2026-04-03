##Crie uma função chamada executar_pipeline que recebe uma lista de dados e uma função de transformação. A função deve aplicar a transformação em cada item da lista e retornar o resultado. Crie duas funções de transformação, uma que dobra um número e outra que adiciona 5. Use sua função executar_pipeline para aplicar primeiro a função que dobra na lista [1, 2, 3], depois aplique a função que adiciona 5 no resultado anterior. Imprima o resultado de cada aplicação.
def executar_pipeline(lista,transformacao):
    return [transformacao (item) for item in lista]
dados = [1,2,3]
def dobra (elemento):
    return elemento * 2
def add (elemento):
    return elemento + 5
def add2 (elemento):
    return elemento + 10
print(f"Elementos da lista dobrados:{executar_pipeline(dados, dobra)} ")
print(f"Elementos da lista + 5:{executar_pipeline(dados, add)}")
print(f"Elementos da lista +5 do resultado anterior:{executar_pipeline(dados, add2)} ")