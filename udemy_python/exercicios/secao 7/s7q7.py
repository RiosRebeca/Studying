print("EXERCÍCIOS - SEÇÃO 7")

# s7q7

'''
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra.
'''

cesta = []
sacola = []

for n in range(11):
    sacola = int(input("Digite um número: "))
    cesta.append(sacola)

cesta.sort()
print(cesta)

for indice, valor in enumerate(cesta):
    print(indice, valor)