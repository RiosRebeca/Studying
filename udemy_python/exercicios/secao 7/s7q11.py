print("EXERCÍCIO - SEÇÃO7")

'''
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.
'''

sacola = []
cesta = []


for vezes in range(10):
    numero = int(input("Insira um número: "))
    if numero < 0:
        sacola.append(numero)
    else:
        cesta.append(numero)

print(sacola)
print(cesta)S
s_np = sum(cesta)
print(s_np)
