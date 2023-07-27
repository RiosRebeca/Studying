print("EXERCÍCIOS - SEÇÃO 7")

'''
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores na ordem inversa.
'''

cesta = []

for vezes in range(6):
    valores = int(input("Digite um valor: "))
    if valores % 2 == 0:
        cesta.append(valores)

print(cesta)  
cesta.reverse()       # ou print(cesta[::-1])
print(cesta)