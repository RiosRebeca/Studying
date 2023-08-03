print("EXERCÍCIO - SEÇÃO 7")

# s7q28

'''
Faça um programa que receba 6 números inteiros e mostre:
--> Os números pares digitados;
--> A soma dos números pares digitados;
--> Os números ímpares digitados;
--> A quantidade de números ímpares digitados

'''

numeros = []

for i in range(6):
    m = int(input("INSIRA UM NÚMERO: "))
    numeros.append(m)

n_pares = []
n_impares = []

for j in numeros:
    if j % 2 == 0:
        n_pares.append(j)
    else:
        n_impares.append(j)

print(f'Os numeros pares são:{n_pares} e o resultado de sua soma é {(sum(n_pares))}).')
print(f'Os numeros ímpares são:{n_impares} e o resultado de sua soma é {(sum(n_impares))}).')