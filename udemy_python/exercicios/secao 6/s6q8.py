print("EXERCÍCIO - SEÇÃO 6")

# s6q8

n_maximo = 0
n_minimo = 1000000000000000000000000000

for a in range(10):
    numero = int(input("Insira um número: "))
    if numero > n_maximo:
        n_maximo = numero
    if numero < n_minimo:
        n_minimo = numero

print(n_maximo, n_minimo)
    
    





'''
eu quero printar o maior input e o menor input
'''