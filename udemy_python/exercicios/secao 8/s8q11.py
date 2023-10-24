print("EXERCÍCIO - SEÇÃO 8")

'''
S8Q11
Elabore uma função que receba três argumento de um aluno como parâmetros e uma letra. Se a letra for A,  função deverá calcular a média aritimética das notas do aluno; se for P, deverá calcular a média pomderada, com pesos 5, 3 e 2.
'''

prova1 = int(input("INSIRA A NOTA DA 1ª PROVA: "))
prova2 = int(input("INSIRA A NOTA DA 2ª PROVA: "))
prova3 = int(input("INSIRA A NOTA DA 3ª PROVA: "))
letra = input("INSIRA UMA 'A' OU 'P': ")

def nota_final(prova1: int, prova2: int, prova3: int, letra: str):
    if letra == 'A':
        return (prova1 + prova2 + prova3)//3
    elif letra == 'P':
        return (prova1*5 + prova2*3 + prova3*2)//3 



print(nota_final(prova1, prova2, prova3, letra))