'''
O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. 
O processo de leitura deve ser encerrado quando o usuário informar o valor zero. 
Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.
'''

soma_impar = 0
soma_par = 0

while True:

    numero = int(input('Insira um numero inteiro qualquer: '))
    
    if numero == 0:
        break
    elif numero % 2 == 0:
        soma_par += 1
        print(f'Você digitou {soma_par} números pares')
    else:
        soma_impar +=1
        print(f'Você digitou {soma_impar} números ímpares')