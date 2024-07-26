'''
Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, 
isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas
'''

while True:
    lado1 = float(input('Digite o comprimento do primeiro lado: '))
    lado2 = float(input('Digite o comprimento do segundo lado: '))
    lado3 = float(input('Digite o comprimento do terceiro lado: '))

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print('Os comprimentos dos lados devem ser maiores que zero.')
        continue
    elif lado1 == lado2 == lado3:
        print('Este triângulo é equilátero.')
    elif lado1 != lado2 and lado3 != lado2 and lado3 != lado1:
        print('Este triângulo é escaleno')
    else:
        print('Este triângulo é isósceles.')