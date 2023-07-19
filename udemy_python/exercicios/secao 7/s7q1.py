print("EXERCÍCIO - SEÇÃO 7")

# s7q1

'''
Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:

1- Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.

2- Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0] e A[5] do vetor e mostre na tela esta soma.

3 - Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.

4- Mostre na tela cada valor do vetor A, um em cada linha.
'''

a = [1, 0, 5, -2, -5, 7]
soma = int(a[0]) + int(a[5])

print(soma)

a.insert(4, 100)     # .insert(posição, argumento)
print(a)

for mostre in a:
    print(mostre)

# a.append[4(100)]
# A lógica tá errada, .append() não é usado para subtituir uma posição

