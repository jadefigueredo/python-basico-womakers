'''
Escreva um programa que calcule o tempo de uma viagem.
Faça um comparativo do mesmo percurso de avião, carro e ônibus. 
Levando em consideração:

avião = 600 km/h
carro = 100 km/h
ônibus = 80 km/h
'''

d = float(input('Escreva a distancia da sua sua viagem em km: '))

dva = float(d/600) # distância da viagem de avião
dvc = float(d/100) # distância da viagem de carro
dvn = float(d/80) # distância de viagem de carro


print(f'A distância de avião é {dva}')
print(f'A distância de carro é {dvc}')
print(f'A distância de ônibus é {dvn}')

if dva > dvc < dvn:
    print('A viagem mais rápida é de avião.')
elif dvc > dva < dvn:
    print('A viagem mais rápida é de carro.')
else:
    print('A viagem mais rápida é de ônibus.')

