print("EXERCÍCIO - SEÇÃO7")

# s7q26

'''
Leia 10 números inteiros e armazene um vetor. Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.
'''

numeros = []
n_primos = []

for i in range(10):
    n = int(input("INSIRA UM NÚMERO: "))
    numeros.append(n)
  
for indice, elemento in enumerate(numeros):
    print(f'O elemento {elemento} está na posição {indice}.')





print(numeros)
print(n_primos)