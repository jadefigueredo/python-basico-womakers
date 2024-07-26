'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

while True:
    nota = float(input('Digite uma nota de zero a dez. '))
    if nota < 0 or nota > 10:
        print('Valor inválido, por favor digite um valor de 0 a 10')
        continue
    else:
        break