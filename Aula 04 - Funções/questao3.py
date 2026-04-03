##Crie uma função chamada calcular_area que receba largura e altura como parâmetros e tenha um valor padrão de 1 para altura. Exiba a área.
def calcular_area(larg, alt=1):
    area = (alt * larg)
    print(f"O valor da área é {area}")
largura = int(input("Digite o valor da largura: "))
areas = calcular_area(largura)