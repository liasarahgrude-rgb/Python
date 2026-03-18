##Crie um programa em Python que cadastre alunos e suas notas em diferentes matérias. O programa deve: 1. Permitir cadastrar o nome de um aluno. 2. Associar um dicionário com matérias e notas desse aluno. 3. Exibir todos os alunos cadastrados com suas notas. Passo a passo da implementação: Criar um dicionário vazio alunos para armazenar os dados Criar um loop infinito (while True) para cadastrar múltiplos alunos Solicitar o nome do aluno com input() e usar .strip() para remover espaços Verificar se o usuário digitou "sair" para encerrar o programa Criar um dicionário vazio materias para as notas do aluno atual Criar outro loop infinito para cadastrar múltiplas matérias Solicitar o nome da matéria e verificar se digitou "fim" para parar Solicitar a nota da matéria e converter para float() Armazenar a matéria e nota no dicionário materias Associar o aluno e suas matérias no dicionário principal alunos Exibir todos os alunos cadastrados usando loop for aninhado Iterar pelos alunos e suas respectivas notas para mostrar os resultados Saida esperada: --- Cadastro de Alunos --- Aluno: Mônica História: 9.0 Geografia: 7.0 Aluno: Lucas História: 5.0 Geografia: 8.0
alunos = {}
while True:
    nome = input ("Digite o nome do aluno ou sair: ").lower()
    if nome == "sair":
        break
    materias = {}
    while True:
        materia = input ("Digite a materia ou fim: ").lower()
        if materia == "fim":
            break
        nota = float (input(f"Digite a nota da materia {materia}: "))
        materias[materia] = nota
    alunos [nome] = materias 
for aluno, notas in alunos.items():
    print(f"\nAluno: {aluno}")
    for materia, nota in notas.items():
        print(f"{materia}:{nota}")