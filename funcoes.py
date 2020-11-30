import mysql.connector

mydb = mysql.connector.connect(user='root', password='diego123',
                              host='127.0.0.1',
                              database='biblioteca')

def login(login, senha):
    myCursor = mydb.cursor()
    myCursor.execute("SELECT senha FROM usuarios WHERE login = %s", (login,))
    myresult = myCursor.fetchone()
    if myresult:
        if (str(myresult[0]) == str(senha)):
            return 'pass'
        else:
            print('Senha errada')
    else:
            print('Usuário não existe')
    return ''

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

def gerarRelatorioLivros():
    myCursor = mydb.cursor()
    myCursor.execute("SELECT * FROM livros")
    myresult = myCursor.fetchall()
    if myresult:
        for livro in myresult:
            print(livro)
    else:
        print('Nenhum livro cadastrado')
        
def gerarRelatorioCategoria():
    myCursor = mydb.cursor()
    myCursor.execute("SELECT * FROM categorias")
    myresult = myCursor.fetchall()
    if myresult:
        for categoria in myresult:
            print(categoria)
    else:
        print('Nenhuma categoria cadastrada')
        
def gerarRelatorioTematica():
    myCursor = mydb.cursor()
    myCursor.execute("SELECT * FROM tematicas")
    myresult = myCursor.fetchall()
    if myresult:
        for tematica in myresult:
            print(tematica)
    else:
        print('Nenhuma categoria cadastrada')

def buscarExemplar(livro):
    myCursor = mydb.cursor()
    myCursor.execute("SELECT * FROM livros WHERE nome = %s", (livro,))
    myresult = myCursor.fetchone()
    if myresult:
        print(myresult)
    else:
        print('Exemplar não encontrado')
