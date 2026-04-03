##Escreva uma função que simule um caixa eletrônico. A função saque deve receber o saldo atual da conta e o valor do saque. Ela deve verificar se o saldo é suficiente para o saque. Se for, deve imprimir 'Saque de R$ [valor] realizado com sucesso!' e o novo saldo. Se não for, deve imprimir 'Saldo insuficiente.' e o saldo atual. Chame a função para dois cenários: um com saque válido e outro com saque inválido.
def checar():
    val_saldo = float(input(f"Digite o valor do seu saldo: "))
    val_saque= float(input(f"Digite o valor que você deseja sacar: "))
    if val_saldo >  val_saque:
        diferenca = val_saldo - val_saque
        print(f"Saque de R$ {val_saque} realizado com sucesso!")
        print(f"O novo valor do seu saldo é {diferenca}")
    else:
        print(f"Saldo insuficiente.")
        print(f"O valor do seu saldo é {val_saldo}")
pessoa = int(input("Quantas pessoas desejam sacar dinheiro?"))
for pessoas in range(pessoa):
    checar()