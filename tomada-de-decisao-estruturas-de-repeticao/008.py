'''
Faça um programa que peça dois números e imprima o maior deles.
'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite outro número inteiro: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número.')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número.')
else:
    print(f'{n3} é o maior número.')