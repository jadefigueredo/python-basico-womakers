'''
Crie um programa que solicite ao usuário um login e uma senha. 
O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.
'''


while True:
    admin = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if admin == 'admin' and senha == 'admin123':
        print('Login efetuado com sucesso!')
        break
    else:
        print('Usuário ou senha inválidos. Tente novamente.')