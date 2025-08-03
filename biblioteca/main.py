from livro import Livro
from biblioteca import Biblioteca
from usuario import Usuario

#Cria uma instancia da classe Biblioteca
biblioteca = Biblioteca()

#cria alguns livros de exemplo:
livro1 = Livro('1984', 'George Orwell', 1949, '978-0451524935')
livro2 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Ecupéry', 1943, '978-0156012195')
livro3 = Livro('Dom Quixote', 'Miguel de Cervantes', 1605, '978-8491050132')

# Adiciona os livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Lista todos os livros na biblioteca:
biblioteca.listar_livros()

# Busca um livro pelo isbn:
isbn_busca = '1234567890'
livro_encontrado = biblioteca.buscar_livro(isbn_busca)
if livro_encontrado:
    print(f'Livro encontrado: {livro_encontrado}')
else: 
    print(f'Livro com ISBN {isbn_busca} não encontrado.')
    
# Remove um livro:
isbn_remover = '0987654321'
biblioteca.remover_livro(isbn_remover)
print('\nApós remover o livro:')
biblioteca.listar_livros()

# Teste de entrada de um novo usuario:
print('\nCadastro de um novo usuário:')
nome = input('Digite o nome do usuário: ')
email = input('Digite o email do usuário: ')
id_usuario = input('Digite o ID do usuário: ')

# Cria o objeto Usuario com os dados fornecidos:
usuario = Usuario(nome, email, id_usuario)

# Exibe os detalhes do usuário:
print('\nUsuário cadastrado com sucesso!')
print(usuario)


# Locação de umlivro para um usuario:
print(f'\nLocação de livro para o usuario {usuario.nome}: ')
livro_para_emprestar = input('Digite o código ISBN do livro a ser emprestado: ')

#Busca o livro na biblioteca:
buscar_livro_emprestado = biblioteca.buscar_livro(livro_para_emprestar)

if buscar_livro_emprestado:
    usuario.empresstar_livro(buscar_livro_emprestado)
    print(f'\nLivro "{buscar_livro_emprestado.titulo}" emprestado por {usuario.nome}.')
else:
    print('Livro não encontrado na biblioteca.')
    
# Lista todos os livros emprestados pelo usuário:
print(f'\nLivros atualmente emprestados pelo usuário {usuario.nome}:')
usuario.listar_livros_emprestados()
        
# Devolução de um livro emprestado:
print(f'\nDevolução de livro por {usuario.nome}: ')
isbn_devolver = input('Digite o código ISBN do livro a ser devolvido: ')

# Procura o livro na lista de livros emprestados pelo usuario:
# Definindo um valor padrão (None) para o livro a ser devolvido
livro_para_devolver = None
# Iterando sobre os livros emprestados pelo usuário para encontrar o livro a ser devolvido
for livro in usuario.livros_emprestados:
    if livro.isbn == isbn_devolver:   # Se o código ISBN do livro coincidir com o fornecido
        # Se encontrado, atribui o livro à variável livro_para_devolver
        livro_para_devolver = livro
        break
    
if livro_para_devolver:
    # Se o livro for encontrado, chama o método devolver_livro do usuário
    usuario.devolver_livro(livro_para_devolver)
    print(f'\nLivro {livro_para_devolver.titulo} devolvido por {usuario.nome}.')
else: 
    print('\nEste livro não está emprestado por este usuário ou não foi encontrado.')
    
# Lista novamente todos os livros emprestados pelo usuário após a devolução:
print(f'\nLivros atualmente emprestados pelo usuário {usuario.nome} após devolução: ')
usuario.listar_livros_emprestados()
    