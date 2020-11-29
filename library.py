import mysql.connector

mydb = mysql.connector.connect(user='root', password='123',
                              host='127.0.0.1',
                              database='biblioteca')

def cadastrarNovoLivro(livro, ano, categoriaId, tematicaId, quantidade):
    myCursor = mydb.cursor()

    sql = ("INSERT INTO livros "
            "(nome, ano, reservado, categoriaId, tematicaId, quantidade, quantidadeReservada) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    val = (livro, ano, 0, categoriaId, tematicaId, quantidade, 0)

    myCursor.execute(sql, val)
    mydb.commit()
    print(myCursor.rowcount, " record inserted")
    myCursor.close()

def cadastrarCategoria(categoria):
    myCursor = mydb.cursor()
    myCursor.execute("INSERT INTO categorias (nome) VALUES (%s)", (categoria,))
    mydb.commit()
    print(myCursor.rowcount, " record inserted")
    myCursor.close()

def cadastrarTematica(tematica):
    myCursor = mydb.cursor()
    myCursor.execute("INSERT INTO tematicas (nome) VALUES (%s)", (tematica,))
    mydb.commit()
    print(myCursor.rowcount, " record inserted")
    myCursor.close()

def adicionarQuantidadeLivro(nome, quantidade):
    myCursor = mydb.cursor()
    myCursor.execute("SELECT quantidade FROM livros WHERE nome = %s", (nome,))
    myresult = myCursor.fetchall()
    if myresult:
        myresult = myresult[0][0] + int(quantidade)
    print(myresult)
    myCursor.close()

    myCursor = mydb.cursor()
    myCursor.execute("UPDATE livros SET quantidade = %s WHERE nome = %s", (myresult, nome))
    mydb.commit()
    print(myCursor.rowcount, " record inserted")
    myCursor.close()
                
def addTituloReserva(nome, reservado):
    myCursor = mydb.cursor()
    myCursor.execute("UPDATE livros SET reservado = %s WHERE nome = %s", (reservado, nome))
    mydb.commit()
    print(myCursor.rowcount, " record updated")
    myCursor.close()

def removerTitulo(nome):
    myCursor = mydb.cursor()
    myCursor.execute("DELETE FROM livros WHERE nome = %s", (nome,))
    mydb.commit()
    print(myCursor.rowcount, " record deleted")
    myCursor.close()

def adicionarReserva(nomePessoa, idLivro):
    myCursor = mydb.cursor()
    myCursor.execute("SELECT quantidadeReservada, quantidade FROM livros WHERE id = %s", (idLivro,))
    myresult = myCursor.fetchall()
    if myresult:
        if myresult[0][0] >= myresult[0][1]:
            print('Reserva máxima')
            return
        myresult = myresult[0][0] + 1
    print(myresult)
    myCursor.close()

    myCursor = mydb.cursor()
    myCursor.execute("UPDATE livros SET quantidadeReservada = %s WHERE id = %s", (myresult, idLivro))
    mydb.commit()
    print(myCursor.rowcount, " record inserted")
    myCursor.close()

    myCursor = mydb.cursor()
    myCursor.execute("INSERT INTO reservas (nomePessoa, idLivro) VALUES (%s, %s)", (nomePessoa, idLivro))
    mydb.commit()
    print(myCursor.rowcount, " record inserted")
    myCursor.close()



# def adcQntTitulo():
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


if __name__ == '__main__':
    adicionarReserva('Marcos', 1)

    # cadastrarNovoLivro('Mamãe Falei', 2010, 2, 3, 1)
    # cadastrarCategoria('Livro Didático')
    # cadastrarCategoria('Enciclopédia')
    # cadastrarCategoria('Dicionário')
    # cadastrarCategoria('Revista Científica')
    # cadastrarCategoria('História em quadrinhos')
    # cadastrarTematica('Álgebra')
    # cadastrarTematica('Gramática')
    # cadastrarTematica('Biologia')

    # print(categorias)
    # print(tematicas)

    # cadastrarNovoLivro('Mamãe Falei', '2010', 2, 3, 1)
    # cadastrarNovoLivro('Olavo', '2010', 1, 2, 5)
    # cadastrarNovoLivro('Teste', '2100', 1, 2, 3)
    # cadastrarNovoLivro('Vars', '2020', 1, 1, 6)
    # cadastrarNovoLivro('Awew', '2020', 2, 2, 3)
    # cadastrarNovoLivro('TT', '2030', 2, 3, 2)

    # removerTitulo('Mamãe Falei')
    # addTituloReserva('Olavo', 1)
    # print(livros)

    # login = input('Qual seu login? ')
    # senha = input('Qual sua senha? ')
    # for f in funcionarios:
    #     if (f.get('login') == login and f.get('senha') == senha):
    #         print('Usuário logado')
    #         main()
    #     else:
    #         print('Senha ou usuário errada')