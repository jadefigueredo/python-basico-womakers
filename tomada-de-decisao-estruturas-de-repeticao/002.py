'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar M - matutino ou V - vespertino ou N - noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = input('Qual turno em que você estuda? M para matutino, V para vespertino e N para noturno. ').upper()

if turno not in ['M', 'V', 'N']:
    print('Turno inválido. Informe M, V ou N.')
elif turno.upper() == 'M':
    print('Bom dia!')
elif turno.upper() == 'V':
    print('Boa tarde!')
elif turno.upper() == 'N':
    print('Boa noite!')