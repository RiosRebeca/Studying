print("EXERCÍCIO - SEÇÃO 8")

'''
S8Q3
Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se for positivo, -1 se negativo e 0 se for igual a 0.
'''


num_positivo = []
num_negativo = []

def tipo_num(numero: int):
    if numero >= 1:
        num_positivo.append(numero)
        return 1
    elif numero < 0:
        num_negativo.append(numero)
        return -1
    return 0

print(tipo_num(numero = 1))
print(tipo_num(numero = -1))
print(tipo_num(numero = -2))
print(tipo_num(numero = 3))
print(tipo_num(numero = 7))
print(tipo_num(numero = 0))

print(num_positivo)
print(num_negativo)