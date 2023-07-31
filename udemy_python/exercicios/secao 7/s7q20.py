print("EXERCÍCIO - SEÇÃO 7")

# s7q20

'''
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela od dados do vetor C.
'''

a = []
b = []

for x in range(10):
    n = int(input("Insira um número: "))
    a.append(n)

for y in range(10):
    m = int(input("Insira um número: "))
    b.append(m)

c = a + b

print(a)
print(b)
print(c)