##Processar as informações: Verificar se o funcionário é maior de idade (18 anos ou mais) Calcular o salário anual (salário mensal × 12) Exibir um relatório final contendo: Dados pessoais do funcionário Se ele é maior de idade Salário anual Instruções técnicas: Use a função input() para capturar os dados Use int() para converter a idade Use float() para converter o salário Use estruturas condicionais (if, elif, else) para as verificações
nome = input("Digite o seu nome completo: ")
idade = input("Digite a sua idade: ")
idade2 = int(idade[0:2])##Caso a pessoa digite "18 anos", o programa irá pegar somente os dois primeiros caracteres, ou seja, "18" e converter para inteiro.
salario = float(input("Digite o seu salario mensal: "))
salarioanual = salario * 12
print(f"---Relatorio Final---")
if idade2 >= 18:
    print(f"O usuario é maior de idade e tem salário anual igual a {salarioanual} ")
elif idade2 < 18:
    print(f"O usuario é menor idade e tem salário anual igual a {salarioanual} ")