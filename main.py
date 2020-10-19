livros = []


def cadastrarNovoLivro(livro, categoria, ano):
    global livros
    livros.append( {
        "nome": livro,
        "categoria": categoria,
        "ano": ano
    } )

#
# def cadastrarCategoriaTematica():
#
# def addTitulo():
#
# def attQntTitulo():
#
# def removerTitulo():
#
# def buscarExemplar():
#
# def importarDados():
#
# def obterStatus(livro):
#
# def gerarRelatorio():
#
# def gerarRelatorioCategoria():
#
# def gerarRelatorioTematica():
#

if __name__ == '__main__':
    cadastrarNovoLivro('Harry Potter', 'Viadagem', '1995')
    cadastrarNovoLivro('Crepusculo', 'Viadagem', '1924')
    cadastrarNovoLivro('A culpa é das estrelas', 'Viadagem', '9999')
