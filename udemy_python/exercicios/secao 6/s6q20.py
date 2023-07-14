print("EXERCÍCIO - SEÇÃO 6")

# s6q20

'''
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados lidos e número de valores pares. O processo termina quando for digitado o número 1000.

--> criar duas variáveis
--> input de valores int (+ de uma vez)
--> 
'''

n_impar = 0
n_par = 0 
n_total = 0 

numero = int(input("Insira um número: "))

while numero != 1000:
    numero = int(input("Insira um número: "))
    n_total += 1
    print(f'A quantidade de números liddos foi: {n_total}')
    if numero % 2 == 0:
        n_par += numero
    elif numero % 2 == 1:
        n_impar += numero
print(f'A quantidade de números pares foi: {n_par}\n    A quantidade de números ímpares foi: {n_impar}\n    O total de números lidos foi: {n_total}')   


'''
n_impar = 0
n_par = 0 
n_total = 0 

while numero != 1000:
    numero = int(input("Insira um número: "))
    n_total += 1
    print(f'A quantidade de números liddos foi: {n_total}')
    if numero % 2 == 0:
        n_par += numero
    elif numero % 2 == 1:
        n_impar += numero
print(f'A quantidade de números pares foi: {n_par}\n    A quantidade de números ímpares foi: {n_impar}\n    O total de números lidos foi: {n_total}')  

--> Aqui teve erro de lógica porque não tem uma condição para interromper o loop uma vez que o numero != 1000 não conta 
'''
