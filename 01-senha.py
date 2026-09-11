nome = str(input("digite seu usuário: "))
senha = str(input("digite sua senha: "))
senha_real = '123'
nome_real = 'pretti'

while senha != senha_real or nome != nome_real:
    print ('Senha incorreta! Tente novamente: ')
    print ('Nome de usuario incorreto! Tente novamente: ')
    senha = input ('Digite sua senha: ')
    nome = input ('Digite seu usuario: ')

print ('Bem vindo ao sistema...')