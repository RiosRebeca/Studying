print("EXERCÍCIO - SEÇÃO 8")


'''
Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".

'''
# Não se intera um int, tem que conberter em list

# numero = int(input("INSIRA UM NÚMERO: "))

def rec_int(a: int):
    res = 0
    if a <= 0:
        return "Número inválido"
    for i in str(a):
        res += int(i)
    return(res)
    

print(rec_int(11235))