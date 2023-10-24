print("EXERCÍCIO - SEÇÃO 8")

'''
S8Q10
Faça uma função que receba dois números e retorne qual deles é o maior.
'''

a = int(input("INSIRA O VALOR DE A: "))
b = int(input("INSIRA O VALOR DE B: "))

def num_maior(a: int, b: int):
    if a >  b:
        return a
    return  b

print(num_maior(a, b))        # Não esquecer de colocar os parâmetros aqui


