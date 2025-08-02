##cria um módulo chamado livro.py que contém uma classe Livro

class Livro: 
    ##Construtor da classe Livro
    ##Recebe título, autor, ano de publicação e ISBN como parâmetros
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