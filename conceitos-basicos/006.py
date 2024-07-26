'''
Solicite ao usuário o peso em kg e a altura em metros. 
Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura x altura).
'''

while True:
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    calcula_imc = peso / altura **2
    print(f'Seu IMC é {calcula_imc:.1f}.')
    break
