##Você recebeu um dicionário que mapeia países e suas respectivas populações: populacoes = {"Brasil": 215_000_000, "China": 1_400_000_000, "EUA": 333_000_000, "Índia": 1_220_000_000} Seu objetivo é descobrir qual país possui a maior população usando um loop for. Passo a passo sugerido: Crie duas variáveis de controle: Uma para guardar o nome do país com maior população (ex: pais_maior_pop), iniciando com uma string vazia. Outra para guardar o valor da maior população encontrada até agora (ex: maior_pop), iniciando com 0. Percorra o dicionário com um for, acessando o país e sua população. A cada iteração, compare a população atual com o valor de maior_pop: Se a população atual for maior, atualize as duas variáveis (maior_pop e pais_maior_pop). Ao final do laço, exiba na tela o resultado no formato: O país com a maior população é: X com Y habitantes.
populaçoes = {'Brasil': 215_000_000, 'China': 1_400_000_000, 'EUA': 333_000_000, 'Índia': 1_220_000_000}
pais_maior_pop = ""
maior_pop = 0
for pais,pop in populaçoes.items():
    if pop > maior_pop:
        maior_pop = pop
        pais_maior_pop = pais
print(f"O {pais_maior_pop} tem a maior população com {maior_pop}")