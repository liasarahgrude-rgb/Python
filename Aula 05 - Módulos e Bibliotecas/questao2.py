##Você deve criar um script chamado utilizando_modulos.py que resolva as seguintes tarefas. O objetivo é entender como usar diferentes módulos internos em conjunto para automatizar pequenas rotinas. Requisitos: Módulo math Peça ao usuário um número inteiro e mostre: O fatorial desse número. A raiz quadrada desse número. Módulo random Crie uma lista com pelo menos 5 nomes e sorteie um deles para exibir na tela. Módulo datetime Mostre a data e a hora atuais. Mostre também apenas o ano atual. Módulo os Mostre qual é o diretório atual do script. Crie uma pasta chamada "resultado_modulos" dentro desse diretório. Organize o código em um único arquivo (utilizando_modulos.py) e utilize os módulos exatamente como visto em aula.
import math
import random
import datetime
import os
numero = int(input("Digite um numero: "))
math.factorial(numero)
# Módulo random Crie uma lista com pelo menos 5 nomes e sorteie um deles para exibir na tela.
lista = [ "Ana","Lia", "Joana", "Lua", "Bia"]
print(random.choice(lista))
##Módulo datetime Mostre a data e a hora atuais.
agora = datetime.datetime.now()
print(f"{agora.hour}, {agora.date()}")
##Módulo os Mostre qual é o diretório atual do script.
diretorio_atual = os.getcwd()
print(f"{diretorio_atual}")