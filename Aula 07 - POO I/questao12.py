##Uma Turma tem alunos. Um Aluno é um objeto independente (agregação), mas a Matricula é um registro que só existe dentro da Turma (composição) para associar um aluno a ela. A nota do aluno deve ser validada. Instruções: Crie a classe Aluno (simples, só com nome). Crie a classe Matricula. Ela recebe um objeto Aluno (agregação) e tem uma propriedade @property para a nota, que deve ser um valor entre 0 e 10. Crie a classe Turma. No construtor, crie uma lista vazia para Matriculas. Na classe Turma, crie um método matricular(aluno) que cria uma Matricula (composição) e a adiciona à lista. Adicione um método exibir_alunos_e_notas() para mostrar os resultados.

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Matricula:
    def __init__(self, aluno):
        self.aluno = aluno   
        self._nota = 0
    @property#O property é como um portão mágico que protege a variável oculta _nota. Ele permite que a gente leia a nota, mas para escrever nela, temos que passar por um filtro de segurança.
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, valor):
    # 🛡️ O FILTRO DE SEGURANÇA:
        if 0 <= valor <= 10:
        # Se a nota for justa, ela entra na variável oculta
            self._nota = valor
        else:
        # Se for absurda, o sistema bloqueia e avisa
            print("Erro: A nota deve ser entre 0 e 10!")

class Turma:
    def __init__(self):
        self.matriculas = []
    def matricular_aluno(self, aluno):
        matricula = Matricula(aluno)
        self.matriculas.append(matricula)
        return matricula
    def exibir_alunos_e_notas(self):
        for matricula in self.matriculas:
            print(f"Aluno: {matricula.aluno.nome}, Nota: {matricula.nota}")
#1. Criamos os alunos
lia = Aluno("Lia Sarah")
Rodrigo = Aluno("Rodrigo")

# 2. Criamos a turma
turma_python = Turma()

# 3. Matriculamos os alunos na turma (Composição)
matricula_lia = turma_python.matricular_aluno(lia)
matricula_rodrigo = turma_python.matricular_aluno(Rodrigo)

# 4. Lançando as notas (usando o @nota.setter com validação)
matricula_lia.nota = 9.5
matricula_rodrigo.nota = 11.0  # Isso vai disparar o aviso de nota inválida e continuará 0

for mat in turma_python.matriculas:
    # Acessamos o nome do aluno indo de: matricula -> aluno -> nome
    print(f"Aluno: {mat.aluno.nome} | Nota: {mat.nota}")
