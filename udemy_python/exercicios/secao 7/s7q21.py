print("EXERCÍCIO - SEÇÃO 7")

# s7q21

'''
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores do primeiro e nas posições impares os valores do segundo.
'''

lista1 = []
lista2 = []

for x in range(10):
    m = int(input("INSIRA OS COMPONENTES DA LISTA 1: "))
    lista1.append(m)

for y in range(10):
    n = int(input("INSIRA OS COMPONENTES DA LISTA 2: "))
    lista2.append(n)

lista3 = []

for z in range(10):
    if z % 2 == 1:
        lista3.append(lista2[z//2])    # Usar uma 'fórmula' no indice para acessar
    else:
        lista3.append(lista1[z//2])    # 

print(lista1)
print(lista2)
print(lista3)

'''
O operador `//` é o operador de divisão inteira em Python. Quando aplicado entre dois números inteiros, ele realiza a divisão e retorna o resultado como um número inteiro, ignorando a parte decimal.


--> Para `z = 0`, `z // 2` será 0. O elemento correspondente em `lista1` é `lista1[0]`, que é 1. Então, 1 é adicionado a `lista3`.

--> Para `z = 1`, `z // 2` será 0 novamente. O elemento correspondente em `lista2` é `lista2[0]`, que é 10. Então, 10 é adicionado a `lista3`.

--> Para `z = 2`, `z // 2` será 1. O elemento correspondente em `lista1` é `lista1[1]`, que é 2. Então, 2 é adicionado a `lista3`.

--> E assim por diante, até `z = 9`.

'''
