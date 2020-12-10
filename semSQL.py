livros = []
funcionarios = [{
    'login': 'admin',
    'senha': '123'
}]
categorias = []
tematicas = []
estoque = []
reservaTitulos = []

def cadastrarNovoLivro(livro, ano, categoriaId, tematicaId, quantidade):
    global livros
    for c in categorias:
        if c.get('id') == categoriaId:
            categoriaNome = c.get('nome')
    for t in tematicas:
        if t.get('id') == tematicaId:
            tematicaNome = t.get('nome')

    livros.append( {
        "id": len(livros) + 1,
        "nome": livro,
        "ano": ano,
        "reservado": 0,
        "categoriaId": categoriaNome,
        "tematicaId": tematicaNome,
        "quantidade": quantidade
    } )

def cadastrarCategoria(categoria):
    global categorias
    categorias.append({
        'id': len(categorias) + 1,
        "nome": categoria,
    })

def cadastrarTematica(tematica):
    global tematicas
    tematicas.append({
        'id': len(tematicas) + 1,
        "nome": tematica
    })

def adicionarQuantidadeLivro(nome, quantidade):
    global livros
    for l in livros:
        if l.get('nome') == nome:
            l['quantidade'] = l.get('quantidade') + quantidade

def addTituloReserva(nome, reservado):
    global livros
    for l in livros:
        if l.get('nome') == nome:
            if (reservado):
                l['reservado'] = 1
            else:
                l['reservado'] = 0

# def adcQntTitulo():
#
def removerTitulo(nome):
    global livros
    for l in livros:
        if l.get('nome') == nome:
            livros.remove(l)

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
def main():
    cadastrarNovoLivro('Harry Potter', 'Viadagem', '1995', '1')
    cadastrarNovoLivro('Crepusculo', 'Viadagem', '1924', '1')
    cadastrarNovoLivro('A culpa é das estrelas', 'Viadagem', '9999', '1')

if __name__ == '__main__':
    cadastrarCategoria('Livro Didático')
    cadastrarCategoria('Enciclopédia')
    cadastrarCategoria('Dicionário')
    cadastrarCategoria('Revista Científica')
    cadastrarCategoria('História em quadrinhos')
    cadastrarTematica('Programação')
    cadastrarTematica('Álgebra')
    cadastrarTematica('Gramática')
    cadastrarTematica('Biologia')

    print(categorias)
    print(tematicas)

    cadastrarNovoLivro('Mamãe Falei', '2010', 2, 3, 1)
    cadastrarNovoLivro('Olavo', '2010', 1, 2, 5)
    cadastrarNovoLivro('Teste', '2100', 1, 2, 3)
    cadastrarNovoLivro('Vars', '2020', 1, 1, 6)
    cadastrarNovoLivro('Awew', '2020', 2, 2, 3)
    cadastrarNovoLivro('TT', '2030', 2, 3, 2)

    removerTitulo('Mamãe Falei')
    addTituloReserva('Olavo', 1)
    print(livros)

    # login = input('Qual seu login? ')
    # senha = input('Qual sua senha? ')
    # for f in funcionarios:
    #     if (f.get('login') == login and f.get('senha') == senha):
    #         print('Usuário logado')
    #         main()
    #     else:
    #         print('Senha ou usuário errada')
