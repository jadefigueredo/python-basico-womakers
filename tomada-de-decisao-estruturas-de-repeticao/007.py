'''
Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.
'''

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Você é uma criança!')
elif idade >= 13 and idade < 18:
    print('Você é um adolescente!')
elif idade >= 18:
    print('Você é um adulto!')
elif idade >= 60:
    print('Você é um idoso!')