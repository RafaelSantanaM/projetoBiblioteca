from livro import Livro
from biblioteca import Biblioteca
from usuario import Usuario

#Cria uma instancia da classe Biblioteca
#   biblioteca = Biblioteca()

# Definindo uma função para cadastro de um livro: 
def cadastrar_livro():
    print('\nCadastro de um novo livro: ')
    # Entrando com as informações do livro :
    titulo = input('Título: ')
    autor = input('Autor: ')
    ano = input('Ano de publicação: ')
    isbn = input('ISBN: ')
    return Livro(titulo, autor, ano, isbn)  #Retorna um objeto livro com os dados fornecidos

# Função para cadastrar um novo usuário: 
def cadastrar_usuario():
    print('\nCadastro de um novo usuário: ')
    nome = input('Nome')
    email = input('Email: ')
    id_usuario = input('ID do usuário: ')
    return Usuario(nome, email, id_usuario)  # Retorna um objeto Usuario com os dados fornecidos

# Função para buscar um livro na biblioteca:
def buscar_livro(biblioteca):
    isbn_busca = input('Digite o código ISBN do livro a ser buscado: ')
    livro_encontrado = biblioteca.buscar_livro(isbn_busca)
    if livro_encontrado:
        print(f'Livro encontrado: {livro_encontrado}')
    else:
        print(f'Livro com ISBN {isbn_busca} não encontrado.')
        
# Função para emprestar um livro:
def emprestar_livro(biblioteca, usuario):
    isbn_emprestimo = input('Digite o código ISBN do livro a ser emprestado: ')
    livro_emprestado = biblioteca.buscar_livro(isbn_emprestimo)
    if livro_emprestado:
        usuario.empresstar_livro(livro_emprestado)
        print(f'Livro "{livro_emprestado.titulo}" emprestado para {usuario.nome}.')
    else:
        print('Livro não encontrado na biblioteca.')
        
# Função para devolver um livro:
def devolver_livro(usuario):
    isbn_devolucao = input('Digite pcódigo ISBN do livro a ser devolvido: ')
    livro_para_devolver = None
    for livro in usuario.livros_emprestados:
        if livro.isbn == isbn_devolucao:
            livro_para_devolver = livro
            break
    if livro_para_devolver:
        usuario.devolver_livro(livro_para_devolver)
        print(f'Livro {livro_para_devolver.titulo} devolvido por {usuario.nome}.')
    else:
        print('Este livro não está emprestado por esse usuário ou não foi encontrado na biblioteca. ')
        print(f'Livros atualmente emprestados por {usuario.nome}:')
        usuario.listar_livros_emprestados()
        
# Função para listar livros da biblioteca: 
def listar_livros(biblioteca):
    print('\nLista de livros na biblioteca: ')
    biblioteca.listar_livros()
    
# Função para listar livros emprestados pelo usuário:
def listar_livros_emprestados(usuario):
    print(f'\nLivros emprestados por {usuario.nome}: ')
    usuario.listar_livros_emprestados()
    
    
# Função principal com menu: 
def main():
    # Cria uma instancia da classe biblioteca: 
    biblioteca = Biblioteca()
    usuarios = []
    
                
                
#cria alguns livros de exemplo:
    livro1 = Livro('1984', 'George Orwell', 1949, '978-0451524935')
    livro2 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Ecupéry', 1943, '978-0156012195')
    livro3 = Livro('Dom Quixote', 'Miguel de Cervantes', 1605, '978-8491050132')

# Adiciona os livros à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    
    usuario = None #inicializa a variável usuario como None
    
    # Criando um loop para o menu:
    while True:
        print('\n---MENU---')
        print('1. Cadastrar livro')
        print('2. Cadastrar usuário')
        print('3. Listar livros na biblioteca')
        print('4. Buscar livro por ISBN')
        print('5. Emprestar livro para usuário')
        print('6. Devolver livro emprestado')
        print('7. Listar livros emprestados pelo usuário')
        print('0. Sair')

        escolha = input('Escolha uma opção: ')
        
        if escolha == '1':
            livro = cadastrar_livro()
            biblioteca.adicionar_livro(livro)
            print(f'Livro "{livro.titulo}" cadastrado com sucesso!')
            
        elif escolha == '2':
            usuario = cadastrar_usuario()
            usuarios.append(usuario)
            print(f'Usuário "{usuario.nome}" cadastrado com sucesso!')
            
        elif escolha == '3':
            listar_livros(biblioteca)
            
        elif escolha == '4':
            buscar_livro(biblioteca)
            
        elif escolha == '5':
            if usuario:
                emprestar_livro(biblioteca, usuario)
            else:
                print('Nenhum usuário cadastrado para emprestar livros.')
                
        elif escolha == '6':
            if usuario:
                devolver_livro(usuario)
            else:
                print('Nenhum usuário cadastrado para devolver livros.')
                
        elif escolha == '7':
            if usuario:
                listar_livros_emprestados(usuario)
            else:
                print('Nenhum usuário cadastrado para listar livros emprestados.')
                
        elif escolha == '0':
            print('Saindo do programa...')
            break
            
        else:
            print('Opção inválida, tente novamente.')

if __name__ == '__main__':
    main()