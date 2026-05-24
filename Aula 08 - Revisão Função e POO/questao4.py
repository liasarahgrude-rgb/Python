##O objetivo deste projeto é refatorar o planejador de refeições feito na última de Streamlit para usar o paradigma da Programação Orientada a Objetos (POO). Em vez de usar apenas funções, você irá organizar o código em classes, que encapsulam dados (atributos) e comportamentos (métodos) relacionados. Sua tarefa é criar um script Python que faça o seguinte: Defina a classe: Crie uma classe chamada PlanejadorRefeicoes. No construtor __init__, inicialize um atributo chamado todos_ingredientes como uma lista vazia. Esta lista pertencerá ao objeto e armazenará todos os ingredientes adicionados. Adicione um método: Crie um método chamado adicionar_refeicao dentro da classe. Este método deve aceitar dois parâmetros: o nome_refeicao (uma string) e os ingredientes (também uma string, com os itens separados por vírgula). Dentro do método, a primeira coisa a fazer é transformar a string de ingredientes em uma lista. Lembre-se de usar a função split(',') e, em seguida, percorrer a lista para remover espaços em branco com strip() e converter tudo para letras minúsculas com lower(). 
# Adicione essa lista de ingredientes à lista geral self.todos_ingredientes. Crie outro método: Adicione um segundo método chamado criar_arquivo que receberá o nome_arquivo como parâmetro. Este método será responsável por processar e salvar os dados. Primeiro, use um set para remover os ingredientes duplicados. Depois, converta o set de volta para uma lista e ordene-a.
# Abra o arquivo especificado para escrita ("w") e escreva um cabeçalho no topo. Finalmente, percorra a lista de ingredientes únicos e escreva cada um em uma nova linha no arquivo. Execute o script: Na seção principal do seu código (sob o if __name__ == "__main__":), crie uma instância da sua classe PlanejadorRefeicoes. Use o método adicionar_refeicao para adicionar três refeições diferentes com seus respectivos ingredientes. Por fim, chame o método criar_arquivo para gerar o arquivo de lista de compras. O objetivo é manter o código pequeno e funcional, mostrando como a POO pode organizar a lógica de forma mais clara.
class PlanejadorRefeicoes:
    def __init__(self):
        self.todos_ingredientes = []
    def adicionar_refeicao (self, nome_refeicao, ingredientes):
        lista = ingredientes.split(',')
        for item in lista:
            ingrediente_limpo = item.strip().lower()
            self.todos_ingredientes.append(ingrediente_limpo)
    def criar_arquivo(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
        ### Remove duplicadas e ordena
        lista_sem_duplicadas = list(set(self.todos_ingredientes))
        lista_ordenada = sorted(lista_sem_duplicadas)
        ##Escrevendo a lista ordenada dentro do arquivo solicitado
        ##"w"= Quero criar um arquivo novo para escrever nele. Se já existir um arquivo com esse nome, apague tudo e comece do zero
        ##Quero criar um arquivo novo para escrever nele. Se já existir um arquivo com esse nome, apague tudo e comece do zero
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            ##Esse for vai pegar um ingrediente por vez dessa lista e guardar temporariamente na variável ingrediente, repetindo o processo até chegar ao fim da lista.
            for ingrediente in lista_ordenada:
                ##"Python, pegue o texto que está aqui dentro dos parênteses e escreva dentro do arquivo".
                arquivo.write(f"{ingrediente}\n")
        
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
if __name__ == "__main__":
    # 1. Criando a instância do planejador
    meu_planejador = PlanejadorRefeicoes()
    
    # 2. Adicionando três refeições diferentes
    meu_planejador.adicionar_refeicao("Café da Manhã", "Pão, Manteiga, Café, Leite")
    meu_planejador.adicionar_refeicao("Almoço", "Arroz, Feijão, Carne, Batata, Salada")
    meu_planejador.adicionar_refeicao("Jantar", "Sopa, Pão, Arroz, Legumes")
    
    # 3. Gerando o arquivo final com a lista de compras
    meu_planejador.criar_arquivo("lista_final.txt")
