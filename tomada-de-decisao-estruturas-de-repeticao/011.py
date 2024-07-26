'''
Escreva um programa que calcule o salário líquido. 
Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
Renda até R$1.903,98: isento de imposto de renda
Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%
Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%
Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%
Renda acima de R$4.664,68: alíquota máxima de 27,5%
'''

salario = float(input('Digite seu salário bruto: '))

if salario >= 1903.98 and salario <= 2826.65:
    desconto_ir = salario * 0.075
    salario_liquido = salario - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')
elif salario >= 2826.66 and salario <= 3751.05:
    desconto_ir = salario * 0.15
    salario_liquido = salario - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')
elif salario >= 3751.06 and salario <= 4664.68:
    desconto_ir = salario * 0.225
    salario_liquido = salario - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')
elif salario > 4664.68:
    desconto_ir = salario * 0.275
    salario_liquido = salario - desconto_ir
    print(f'Seu salário líquido é: {salario_liquido:.2f}')
else:
    print('Você está isento de IR.')