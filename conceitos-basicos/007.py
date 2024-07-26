'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.

'''

valor_hr = float(input('Quanto você ganha por hora de trabalho? '))
horas_trabalhadas = float(input('Quantas horas você trabalhou este mês? '))

salario_bruto = valor_hr * horas_trabalhadas

print(f'Seu salário bruto é: {salario_bruto:.2f}')