print("DESENHOS DA SEÇÃO 8")

'''
Q16 Faça uma função chamada sesenha_linha. Ela deve desenhar uma linha na tela usando símbolos de iguai (ex: =======). A função recebeca por parâmetro quantos sinais de igual serão mostrados.
'''

def desenha_linha():
    n = int(input("Insira o tamanho da linha: "))
    linha = ''
    for i in range(n):
        linha += '='
    return linha     

print(desenha_linha())


'''
Q22 Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos de exclamação, conforme o exemplo abaixo (para n = 5):

!
!!
!!!
!!!!
!!!!!
'''


def pir_exc(n):                  # Cria uma função com parâmetro 'n'
    for i in range(1, n + 1):    # para i; start em 1 e step parâmetro + 1
        print("!" * i)

print(pir_exc(9))



'''
Q23 Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a saída para n = 4 seria:

*
**
***
****
***
**
*

como formar um triângiulo?


1- 1 + n até chegar na LINHA CENTRAL
2- A LINHA CENTRAL É A MAIS LONGA
3- LINHA CENTRAL - 1 até chegar a 1
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
Q24 Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exemplo, a saída para n = 6 seria:

      *
     ***
    *****
   ********
  **********
 ************
'''


