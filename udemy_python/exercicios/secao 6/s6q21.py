print("EXERCÍCIO - SEÇÃO")

# s6q21

'''
Faça um programa que receba dois números. Calcule e mostre:
  a) A soma dos números pares desse intervalo de números, incluindo os números digitados;
  b) a multiplicação dos números ímpares desse intervalo, incluindo os digitados;
'''

n_par = 0
n_impar = 0

tentativas = 0

while tentativas <= 5:
    tentativas += 1
    numero_1 = int(input("Insira um número: "))
        if numero_1 % 2 == 0:
            n_par += numero_1
        if numero_2 % 2 == 0:
     numero_2 = int(input("Insira outro número: "))
   n_par += numero_2
        if numero_1 % 2 == 1:
         if n_impar = n_impar * numero_1
    if numero_2 % 2 == 1:
        n_impar = n_impar * numero_2

print(f'A soma dos números pares é: {n_par}')
print(f'A múltiplicação dos números ímpares é: {n_impar}')