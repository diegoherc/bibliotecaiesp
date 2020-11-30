from funcoes import login
from menu import menuInicio

while 1:
    user = str(input('Digite o usuario: '))
    senha = str(input('Digite o senha: '))

    logar = login(user, senha)

    if (logar == 'pass'):
        menuInicio()
        break