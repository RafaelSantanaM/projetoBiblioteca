from livro import Livro

# Cria uma classe chamada biblioteca
class Biblioteca:
    # O método __init__ é o construtor da classe Biblioteca.
    # Ele é chamado automaticamente quando criamos um novo objeto Biblioteca.
    def __init__(self):
        # Cria um dicionario vazio para armazenar os livros
        #ass chaves serão os códigos ISBN dos livros
        self.livros = {}
        
    # Método para adicionar um livro à biblioteca
    #Parametro:
    #   livro: um objeto da classe Livro
    # Retorna:
    #   None
    def adicionar_livro(self, livro):
    # adiciona ou atualiza o livro ao dicionário pelo isbn
        self.livros[livro.isbn] = livro
        
    # Método para remover um livro da biblioteca pelo ISBN
    # Parâmetro:    
    #   isbn: código ISBN do livro (string)
    # Retorna:
    #   None
    def remover_livro(self, isbn):
        # Verifica se o livro com o ISBN fornecido existe na biblioteca
        if isbn in self.livros:
            # Remove o livro do dicionário
            del self.livros[isbn]
        else:
            # Se o livro não for encontrado, exibe uma mensagem de erro
            print(f'Livro com ISBN {isbn} não encontrado na biblioteca.')
    # Método para buscar um livro pelo isbn:
    # Parâmetro:
    #   isbn: código ISBN do livro (string)
    # Retorna:
    #   O objeto Livro correspondente ao ISBN, ou None se não encontrado
    def buscar_livro(self, isbn):
        # Verifica se o livro com o ISBN fornecido existe na biblioteca
        if isbn in self.livros:
            # Retorna o livro correspondente
            return self.livros[isbn]
        else:
            # Se o livro não for encontrado, retorna None
            return None
        
    # Método para listar todos os livros na biblioteca
    def listar_livros(self):
        # Verifica se há livros na biblioteca
        if not self.livros:
            # Se não houver livros, exibe uma mensagem
            print('Nenhum livro na biblioteca.')
        else:
            # Se houver livros, itera sobre eles e imprime suas representações em string
            for livro in self.livros.values():
                print(f'{livro.titulo} de {livro.autor} ({livro.ano_publicacao}) - ISBN: {livro.isbn}')
            