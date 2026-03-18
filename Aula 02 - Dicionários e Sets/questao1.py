##Crie um dicionário vendas que armazena o número de vendas por vendedor. As chaves são os nomes e os valores são as vendas (ex: {"Ana": 10, "Bruno": 15, "Carla": 8}). Adicione um novo vendedor, "Pedro", com 12 vendas. Depois, remova a vendedora "Carla" do dicionário. Por fim, calcule e imprima a soma total de todas as vendas restantes.
info = {'Ana' : 10, 'Bruno' : 15, 'Carla' : 8}
print(info)
info ['Pedro'] = 12
print(info)
del info["Carla"]
print(info)
soma = sum (info.values())
print(f"A soma das vendas restantes {soma}")