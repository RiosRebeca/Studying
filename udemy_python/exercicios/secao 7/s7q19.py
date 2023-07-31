print("EXERCÍCIOS - SEÇÃO 7")

# s7q19

'''
Escreva um programa que leia números inteiros no intervalo de [0,50] e os armazene em um vetor com 10 posiões. Preencha um segundo vetor apenas com números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
'''

lista = []
n_impares = []

for i in range(50):
    lista.append(i)
    if i % 2 == 1:
        n_impares.append(i)

for i in range(len(n_impares)):
    print(lista.pop(0), n_impares.pop(0))


print(lista)
print(n_impares)