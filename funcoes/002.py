'''
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''

def reverse_number(number):
    return int(str(number)[::-1])

# Teste
print(reverse_number(127))  # Output: 721
