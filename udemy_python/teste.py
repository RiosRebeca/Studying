print("ESPAÇO PARA TESTE")

'''
Q24 Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exemplo, a saída para n = 6 seria:
'''

def piramide(n):
    for i in range(n):
        altura = '@' * i
        altura = ' ' * n
        print(altura)


print(piramide(10))
        
