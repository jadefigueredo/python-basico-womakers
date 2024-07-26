'''
Faça um programa que lê três números inteiros e os mostra em ordem crescente.
'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite outro número inteiro: '))

lista = [n1, n2, n3]
lista.sort()

print(f'Os números em ordem crescente são: {lista}')