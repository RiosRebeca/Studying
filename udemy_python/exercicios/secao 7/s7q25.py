print("EXERCÍCIO - SEÇÃO 7")

# s7q25

'''
Faça um programa que calcule o desvio padrão de um vetor v (xi) contendo n = 10 números, onde m é a média do vetor.

Dp = sqrt(som(xi - x) ** 2) // n)

xi = valor individual
x = média dos valores
n = número de valores

print(f"A média dos valores é {x}.")

'''

import math

n = int(input("INSIRA A QUANTIDADE DE VALORES: "))
s_xi = []

for a in range(n):
    xi = int(input("Qual o valor individual? "))
    s_xi.append(xi)
    x = sum(s_xi)//n                

p_dp = (sum(s_xi) - x) ** 2 // n
dp = math.sqrt(p_dp)

print(f"O valor do Desvio Padrão é de {dp}.")
    