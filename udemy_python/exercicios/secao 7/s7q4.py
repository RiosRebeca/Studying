print("EXERCÍCIO - SEÇÃO 7")

# s7q4

'''
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores x e y quaiquer correpondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições x e y.
'''


a = [(list(range(9)))]        # criou uma lista dentro de uma lista
b = list(range(1,9))          # criou uma lista com 8 elementos
                              # OBS: iniciei com 1 p/ diferenciar na hora do print
print(a)
print(b)

print(b[3])
print(b[5])

soma = (b[3]) + (b[5])        # Aqui eu não preciso transformar para int
print(soma)