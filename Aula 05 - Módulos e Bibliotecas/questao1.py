##Você vai criar um pequeno sistema de calculadora de operações matemáticas organizado em dois arquivos Python. O objetivo é dividir o código em módulos e mostrar como importar funções, tanto de arquivos próprios quanto de bibliotecas internas do Python. Requisitos: Crie um arquivo chamado operacoes.py que contenha pelo menos 3 funções: somar(a, b) → retorna a soma dos números. subtrair(a, b) → retorna a subtração dos números. raiz_quadrada(x) → usa a função sqrt do módulo math para calcular a raiz quadrada. Crie outro arquivo chamado app.py, que será o programa principal. Importe o módulo operacoes. Peça ao usuário dois números inteiros. Mostre na tela o resultado da soma e da subtração usando as funções do módulo. Mostre também a raiz quadrada do primeiro número digitado. Organize o código para que todas as funções fiquem dentro de operacoes.py e apenas a execução do programa fique em app.py.
import operacoes
valorA = int(input("Digite o 1 valor: "))
valorB = int(input("Digite o 2 valor: "))
print(operacoes.soma(valorA, valorB))
print(operacoes.sub(valorA, valorB))
print(operacoes.raiz1(valorA))
