from livro import Livro
from biblioteca import Biblioteca

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