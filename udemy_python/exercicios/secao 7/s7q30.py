print("EXERCÍCIO - SEÇÃO 7")

# s7q30

'''
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. Não deve conter números repetidos.
'''

carrinho = []
carrinho2 = []

for x in range(10):
    n = input("ADICIONE PRODUTOS NO CARRINHO: ")
    carrinho.append(n)

for y in range(10):
    m = input("ADICIONE PRODUTOS NO CARRINHO 2: ")
    carrinho2.append(m)

produtos = set(carrinho).union(set(carrinho2))

print(f'Você adicionou {len(carrinho)} protudos no carrinho 1. São eles: {carrinho}')
print(f'Você adicionou {len(carrinho2)} protudos no carrinho 2. São eles: {carrinho2}')
print(f'Esses são os produtos {(len(produtos))} totais: {produtos}')

# Aqui ele vai fazer a união excluindo os elementos repetidos