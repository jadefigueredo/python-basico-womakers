'''
Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
'''

km_input = (float(input('Insira a quantidade de km percorridos por você: ')))
cm = 100000
m = 1000
mm = 1000000
print(f'{km_input} km equivalem a {km_input * m} em metros, {km_input * cm} em centímetros e {km_input * mm} em milimetros.')
