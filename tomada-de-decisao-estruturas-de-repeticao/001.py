'''
Faça um programa que peça dois números e imprima o maior deles.
'''
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print(f'{n1}')
elif n2 > n1:
    print(f'{n2}')
else:
    print('Os números são iguais.')