print("EXERCÍCIOS - SEÇÃO 7")

# s7q18

'''
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i) % (i + 1), sendo i a posição do elemento no vetor. Em seguida, imprima o vetor na tela.
'''

lista = []

for i in range(50):
   p = (i + 5 * i) % (i + 1)
   lista.append(p)

print(lista)

lista2 = []       # Fazendo o teste

for a in range(100):            # Trocando o range
   p = (a + 5 * a) % (a + 1)
   lista2.append(p)

print(lista2)