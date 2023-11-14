print("ESPEÇO PARA TESTE")


'''
Q23 Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a saída para n = 4 seria:
'''


def triangulo_lateral(n):
    for i in range(n):
        parte_1 = '*' * i
        print(parte_1)
    for j in range(n, 0, - 1):
        parte_2 = '*' * j 
        print(parte_2)

print(triangulo_lateral(4))


'''
como formar um triângiulo?


1- 1 + n até chegar na LINHA CENTRAL
2- A LINHA CENTRAL É A MAIS LONGA
3- LINHA CENTRAL - 1 até chegar a 1



for vai pegar o número do andar no range, se for primeiro andar ele vai fazer andar = '*' * numero do andar 

'''