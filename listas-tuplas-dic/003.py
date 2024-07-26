'''
Crie um dicionário representando um carrinho de compras. 
Adicione produtos (chaves) e quantidades (valores) ao carrinho. 
Calcule o total do carrinho de compra.
'''

carrinho = {}


# Adicionando produtos ao carrinho
carrinho['Camiseta'] = 35
carrinho['Calça'] = 180
carrinho['Bermuda'] = 95

# Calculando o total do carrinho
total = sum(carrinho.values())
print(f'Total do carrinho: R$ {total}')