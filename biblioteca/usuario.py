# Cria classe usuario.py que representa um usuário da biblioteca
class Usuario:
    # O método __init__ é o construtor da classe Usuário.
    # Ele é chamado automaticamente quando criamos um novo objeto Usuário.
    # Parâmetros:
    #   nome: nome do usuário (string)
    #   email: email do usuário (string)
    #   id: identificador único do usuário (int, opcional)
    def __init__(self, nome, email, id_usuario):
        #Atributos da classe:
        self.nome = nome
        self.email = email
        self.id_usuario = id_usuario
        self.livros_emprestados = []
        
    # Método para emprestar um livro ao usuário:
    # Parâmetros:
    #   self: referência ao objeto atual(instância da classe)
    #   livro: um objeto da classe Livro
    def empresstar_livro(self, livro):
        self.livros_emprestados.append(livro)
        
    # Método para devolver um livro emprestado pelo usuário:
    # Parâmetros:
    #   self: referência ao objeto atual(instância da classe)
    #   livro: um objeto da classe Livro
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
        else:
            print(f'O livro {livro.titulo} não está emprestado por {self.nome}.')
    
    # Método para listar todos os livros emprestados pelo usuário:
    # Parâmetros:
    #   self: referência ao objeto atual(instância da classe)
    def listar_livros_emprestados(self):
        if not self.livros_emprestados:
            print(f'{self.nome} não tem livros emprestados.')
        else:
            print(f'Livros emprestados por {self.nome}:')
            for livro in self.livros_emprestados:
                print(f'- {livro.titulo} de {livro.autor} ({livro.ano_publicacao}) - ISBN: {livro.isbn}')    
    
    
    # Método para retornar uma representação em string ao usuário: 
    def __str__(self):
        return f'Usuário: {self.nome}, Email: {self.email}, ID: {self.id_usuario}'