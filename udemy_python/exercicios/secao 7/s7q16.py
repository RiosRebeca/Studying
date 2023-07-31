print("EXERCÍCIO - SEÇÃO 7")

# s7q16

'''
Leia um vetor de 10 posições e atribua calor 0 para todos os elementos que possuírem valores negativos.
'''

lista = []

for b in range(10):
    numero = int(input("INSIRA UM NÚMERO: "))
    if numero > 0 :
        lista.append(numero)
    else:
        lista.append(0)

print(lista)
