print("EXERCÍCIO - SEÇÃO 7")

# s7q27

'''
Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2. Copie os valores ímpares de v para v1 e os valores pares de v para v2. Note que cada um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são utilizados. No final escreva os elementos utilizados de v1 e v2.
'''

v = []

for a in range(10):
    n = int(input("INSIRA UM VALOR: "))
    v.append(n)

v1 = []
v2 = []

for b in v:
    if b % 2 == 1:
        v1.append(b)
    else:
        v2.append(b)

print(f'A lista principal é composta de {len(v)} elementos. São eles:{v}')
print(f'A lista 2 é comporta de {len(v1)} elementos ímpares. São eles:{v1}')
print(f'A lista 3 é composta de {len(v2)} elementos pares. São eles:{v2}')