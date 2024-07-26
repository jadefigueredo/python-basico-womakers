'''
Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
'''

contatos = {
    'Alice': '1234567890',
    'Bob': '9876543210',
    'Carol': '5555555555',
    'David': '3333333333',
    'Eve': '7777777777',
    'Frank': '2222222222',
    'Grace': '4444444444',
    'Harry': '6666666666',
    'Ivy': '1111111111',
    'Jack': '8888888888',
    'Kate': '9999999999',
    'Lisa': '5555555555',
    'Mary': '3333333333'
}

# Imprimindo os nomes dos contatos
contatos.keys()
print(contatos.keys())

busca_nome = input('Digite o nome do contato que deseja encontrar o número: ')

for busca in contatos:
    if busca.lower() == busca_nome.lower():
        print(f'O número do contato {busca} é {contatos[busca]}')
        break