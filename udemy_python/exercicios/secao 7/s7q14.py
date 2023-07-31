print("EXERCÍCIO - SEÇÃO 7")

'''
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.
'''

lista = []
i_repetidos = []

for i in range(20):
    n = int(input("Insira um número: "))
    lista.append(n)

for r in lista:
    repetidos = lista.count(r)
    if repetidos > 1 and not r in i_repetidos:
        i_repetidos.append(r)
        lista2 = list(set(lista))

print(lista)
print(lista2)
print(i_repetidos)

