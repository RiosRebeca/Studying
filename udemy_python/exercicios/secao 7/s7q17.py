print("EXERCÍCIOS - SEÇÃO 7")

# s7q17

'''
Faça um programa que leia o vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num vetor e mostre-os na tela.

--> pra contar os múltiplos tem que x % == 0
'''

lista = []


for i in range(10):
    numero = int(input("INSIRA UM NÚMERO NA LISTA: "))
    lista.append(numero)

multiplos = []
n_multiplos = []

x = int(input("INSIRA UM NÚMERO: "))

for n in lista:
    if n % x == 0:
        multiplos.append(n)
    else:
        n_multiplos.append(n)

print(lista)
print(n_multiplos)    
print(f"O número inserido foi {x} e os seus múltiplos são: {multiplos}")

