nome = ""
senha = ""

print('Digite um nome e uma senha(o nome de usuário não pode ser igual a senha!)')

while True:
    nome = str(input('qual o nome do usuário: '))
    senha = str(input('qual a senha: '))
    if nome == senha:
        print('ERRO, a senha é igual ao nome de usuário')
    else:
        print('tudo certo!')
        break
