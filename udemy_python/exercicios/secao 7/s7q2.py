print("EXERCÍCIOS - SEÇÃO 7")

# s7q2

'''
Crie um programa que lê 6 valores inteiros e, em segida, mostre na tela os valores lidos.
'''

lista = list(range(7))

print(lista)   #output: [0, 1, 2, 3, 4, 5, 6]

for resultado in lista:
    print(resultado)

'''
É importante lembrar como o loop for dunciona. O loop "for" vai PERCORRER cada elemento que foi atribuída a variável (nesse caso, resultado). Esses elementos serão importados da lista, que eu tinha definidor anteriormente como range(7).
'''