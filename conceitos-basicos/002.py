'''
Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
'''

from datetime import date

def calcula_idade():
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    data_atual = date.today()
    ano_atual = data_atual.year
    idade = ano_atual - ano_nascimento
    return idade

print(calcula_idade())