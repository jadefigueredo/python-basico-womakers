'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. 
Considere a tabela de conversão abaixo:
Dólar Americano: R$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suíço: R$0,42
Euro: R$5,36
Libra esterlina: R$6,21
'''

carteira = float(input('Quanto dinheiro em reais você tem na carteira? '))

def calcula_carteira(carteira):
    carteira_dolar_americano = carteira / 4.91
    carteira_peso_argentino = carteira / 0.02
    carteira_dolar_australiano = carteira / 3.18
    carteira_dolar_canadense = carteira / 3.64
    carteira_franco_suico = carteira / 0.42
    carteira_euro = carteira / 5.36
    carteira_libra_esterlina = carteira / 6.21

    return {
        print(f'Dólar Americano: {carteira_dolar_americano:.2f}'),
        print(f'Peso Argentino: {carteira_peso_argentino:.2f}'),
        print(f'Dólar Australiano: {carteira_dolar_australiano:.2f}'),
        print(f'Dólar Canadense: {carteira_dolar_canadense:.2f}'),
        print(f'Franco Suíço: {carteira_franco_suico:.2f}'),
        print(f'Euro: {carteira_euro:.2f}'),
        print(f'Libra Esterlina: {carteira_libra_esterlina:.2f}')
    }

# teste
print(calcula_carteira(carteira))