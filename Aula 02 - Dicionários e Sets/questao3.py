##Imagine que compradores_janeiro é um set com os clientes que compraram em janeiro compradores_janeiro = {"João", "Maria", "Ana", "Carlos"} e compradores_fevereiro é um set com os clientes de fevereiro. compradores_fevereiro = {"Ana", "Pedro", "João", "Juliana"} encontre os clientes que compraram apenas em janeiro. Imprima o resultado.
compradores_janeiro = {"João", "Maria", "Ana", "Carlos"}
compradores_fevereiro = {"Ana", "Pedro", "João", "Juliana"}
jan = compradores_janeiro - compradores_fevereiro
print(f"{jan} só compraram produtos no mês de janeiro!")

compradores_janeiro = {"João", "Maria", "Ana", "Carlos"}
compradores_fevereiro = {"Ana", "Pedro", "João", "Juliana"}
diferenca2 = compradores_janeiro.difference(compradores_fevereiro)
print(f"{diferenca2} só compraram produtos no mês de janeiro!")