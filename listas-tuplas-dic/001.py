soma = 0

resposta = input('Telefonou para a vítima? [S ou N] ')
if resposta.upper() == 'S':
    soma += 1
resposta = input('Esteve no local do crime? [S ou N] ')
if resposta.upper() == 'S':
    soma += 1
resposta = input('Mora perto da vítima? [S ou N] ')
if resposta.upper() == 'S':
    soma += 1
resposta = input('Já trabalhou com a vítima? [S ou N] ')
if resposta.upper() == 'S':
    soma += 1
if soma >= 2:
    print('Sua classificação: Suspeita!')
elif soma >= 3 or soma <= 4:
    print('Sua classificação: Cúmplice!')   
elif soma == 5:
    print('Sua classificação: Assassino!')
else:
    print('Sua classificação: Inocente!')
