from funcoes import *

def menuCadastrarNovoLivro():
    livro = str(input('Nome do livro: '))
    ano = str(input('Ano do livro: '))
    categoriaId = str(input('ID Categoria do livro: '))
    tematicaId = str(input('ID Tematica do livro: '))
    quantidade = str(input('Quantidade existente do livro: '))
    cadastrarNovoLivro(livro, ano, categoriaId, tematicaId, quantidade)
    menuInicio()

def menuCadastrarCategoria():
    categoria = str(input('Nome da categoria a ser cadastrada: '))
    cadastrarCategoria(categoria)
    menuInicio()

def menuCadastrarTematica():
    tematica = str(input('Nome da tematica a ser cadastrada: '))
    cadastrarTematica(tematica)
    menuInicio()

def menuAdicionarQuantidadeLivro():
    livro = str(input('Nome do livro: '))
    quantidade = str(input('Quantidade: '))
    adicionarQuantidadeLivro(livro, quantidade)
    menuInicio()

def menuAdicionarTituloReserva():
    livro = str(input('Nome do livro: '))
    reservado = str(input('Reservado: '))
    addTituloReserva(livro, reservado)
    menuInicio()

def menuRemoverTitulo():
    livro = str(input('Nome do livro: '))
    removerTitulo(livro)
    menuInicio()

def menuAdicionarReserva():
    nomePessoa = str(input('Nome do aluno: '))
    idLivro = str(input('ID do Livro: '))
    adicionarReserva(nomePessoa, idLivro)
    menuInicio()

def menuBuscarExemplar():
    livro = str(input('Nome do livro: '))
    buscarExemplar(livro)
    menuInicio()

def menuInicio():
    print('Bem Vindo a Biblioteca IESP')
    print('Opções (selecione um número):')
    print('(1) Cadastrar novo livro')
    print('(2) Cadastrar categoria')
    print('(3) Cadastrar temática')
    print('(4) Adicionar quantidade livro')
    print('(5) Adicionar título reserva')
    print('(6) Remover Título')
    print('(7) Adicionar Reserva')
    print('(8) Gerar relatório de livros')
    print('(9) Gerar relatório de categorias')
    print('(10) Gerar relatório de temáticas')
    print('(11) Buscar Exemplar')
    print('(12) Sair do Sistema')
    opcao = str(input('Digite sua opção: '))
    
    if opcao == '1':
        menuCadastrarNovoLivro()
    elif opcao == '2':
        menuCadastrarCategoria()
    elif opcao == '3':
        menuCadastrarTematica()
    elif opcao == '4':
        menuAdicionarQuantidadeLivro()
    elif opcao == '5':
        menuAdicionarTituloReserva()
    elif opcao == '6':
        menuRemoverTitulo()   
    elif opcao == '7':
        menuAdicionarReserva()  
    elif opcao == '8':
        gerarRelatorioLivros()
    elif opcao == '9':
        gerarRelatorioCategoria()
    elif opcao == '10':
        gerarRelatorioTematica()
    elif opcao == '11':
        menuBuscarExemplar()
    elif opcao == '12':
        exit()
