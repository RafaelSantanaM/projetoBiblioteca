##cria um módulo chamado livro.py que contém uma classe Livro

class Livro: 
    # O método __init__ é o construtor da classe.
    # Ele é chamado automaticamente quando criamos um novo objeto Livro.
    # Parâmetros:
    #   titulo: título do livro (string)
    #   autor: nome do autor (string)
    #   ano_publicacao: ano em que o livro foi publicado (int ou string)
    #   isbn: código ISBN do livro (string)
    def __init__(self, titulo, autor, ano_publicacao, isbn):
        ##Atributos da classe Livro
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn 
    
    ##Método para retornar uma representação em string do livro
    def __str__(self):
        ##Formata a string com os detalhes do livro 
        return f'{self.titulo} de {self.autor} ({self.ano_publicacao}) - ISBN: {self.isbn}'