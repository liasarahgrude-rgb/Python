##Você está desenvolvendo um sistema para uma biblioteca. A sua tarefa é modelar a relação entre diferentes tipos de publicações usando herança, sobrescrita e a função super(). Instruções: Crie uma classe base chamada Publicacao. O construtor __init__ deve receber titulo e autor e inicializar esses atributos. A classe deve ter um método exibir_info que retorne uma string formatada com o título e o autor. 
# Crie uma subclasse chamada Livro que herda de Publicacao. O construtor __init__ do Livro deve aceitar titulo, autor e numero_paginas. O construtor deve usar a função super() para chamar o construtor da superclasse Publicacao e inicializar os atributos titulo e autor. Em seguida, deve inicializar o atributo numero_paginas na classe Livro. Na classe Livro, sobrescreva o método exibir_info. A nova versão deve primeiro chamar a versão da superclasse usando super().exibir_info() para obter a string com título e autor, e depois concatenar com a informação do número de páginas. Crie uma outra subclasse chamada Revista que também herda de Publicacao. O construtor deve aceitar titulo, autor e edicao. Sobrescreva o método exibir_info para que retorne uma string formatada específica para revistas, incluindo a edição. Dica: Lembre-se que o uso de super() no construtor da subclasse é essencial para garantir que os atributos da superclasse sejam corretamente inicializados.
class Publicacao:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def exibir_info(self):
       return f"Título: {self.titulo}, Autor: {self.autor}"
    
class Livro(Publicacao):
    def __init__(self, titulo, autor,numero_paginas):
        super().__init__(titulo, autor)
        self.numero_paginas = numero_paginas
    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base}, Páginas: {self.numero_paginas}"

class Revista(Publicacao):
    def __init__(self, titulo, autor,edicao):
        super().__init__(titulo, autor)
        self.edicao = edicao
    def exibir_info(self):
        return f"Revista: {self.titulo}, Edição: {self.edicao}, Autor: {self.autor}"
    
    ##Criei os livros
livro1 = Livro("As Crônicas de Nárnia", "C.S. Lewis", 752)
revista1 = Revista("National Geographic", "Editora Abril", 254)

print(livro1.exibir_info())
print(revista1.exibir_info())

