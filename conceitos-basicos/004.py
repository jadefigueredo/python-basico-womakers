'''
Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''

litros_cons = float(input('Digite quantos litros foram consumidos na viagem: '))
km_percorrido = float(input('Digite quantos km foram percorridos: '))

# Calculando o consumo em km/l
consumo_km_l = km_percorrido / litros_cons

print(f'O consumo médio do carro foi de {consumo_km_l:.2f} km/l')