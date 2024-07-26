'''
Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. 
Para cada opção, crie uma função.
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
'''

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    escolha = input('Digite a sua opção desejada: 1. Converter de celsius para farenheit \n 2. Converter de farenheit para celsius. ')
    if escolha == '1':
        celsius = float(input('Digite a temperatura em celsius: '))
        celsius_to_fahrenheit(celsius)
    elif escolha == '2':
        fahrenheit = float(input('Digite a temperatura em farenheit: '))
        fahrenheit_to_celsius(fahrenheit)
    else:
        print('Digite uma opção válida!')