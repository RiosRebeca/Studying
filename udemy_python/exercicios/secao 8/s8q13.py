print("EXERCÍCIO - SEÇÃO 8")

'''
Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo representará a operação que se deseja efetuar com números. Se o símbolo for + deverá ser realizada uma adião, se for - uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação.
'''



def ope_valor(a: int, b: int):
    s = input("INSIRA UM SÍMBOLO: ")
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '/':
        return a//b
    elif s == '*':
        return a * b

print(ope_valor(3, 5))