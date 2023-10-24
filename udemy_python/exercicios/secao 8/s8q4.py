print("EXERCÍCIO - SEÇÃO 8")

'''
S8Q4
Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro não negativo que pode ser expresso como o quadrado d outro número inteiro. Ex: 1, 4, 9...
'''

from math import sqrt

def quadrado_perfeito(numero: int):
    raiz = sqrt(numero)
    if raiz - int(raiz) == 0:
        return f'{numero} é uma raiz perfeita'
    return f'{numero} não é uma raiz perfeita'

print(quadrado_perfeito(numero = 1 ))
print(quadrado_perfeito(numero = 2 ))
print(quadrado_perfeito(numero = 3 ))
print(quadrado_perfeito(numero = 4 ))
print(quadrado_perfeito(numero = 5 ))
print(quadrado_perfeito(numero = 6 ))
print(quadrado_perfeito(numero = 7 ))
print(quadrado_perfeito(numero = 8 ))
print(quadrado_perfeito(numero = 9 ))
print(quadrado_perfeito(numero = 10))
