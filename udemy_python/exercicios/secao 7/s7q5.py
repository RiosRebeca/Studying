print("EXERCÍCIO - SEÇÃO 7")

'''
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possuir.
'''

a = list(range(101))
n_par = []
n_impar = []

for numeros in a:
    if numeros % 2 == 0:
        n_par.append(numeros)
    if numeros % 2 == 1:
        n_impar.append(numeros)

print(n_par)
print(n_impar)

print(len(n_par))    

# Usar o "len" quando quiser saber o comprimento da lista;
# O .count() seria para contar o que está dentro dos ()....

'''

a = list(range(101))
numeros_pares = a.count(lambda x: x % 2 == 0)

print("A quantidade de números pares na lista é:", numeros_pares)

--> Esse foi o chatGPT
A função lambda em Python é uma forma de criar funções anônimas de forma concisa e inline, ou seja, sem a necessidade de definir uma função com um nome específico. Ela é útil quando você precisa de uma função simples que será usada apenas em um contexto específico, como em métodos como map(), filter() e count().

--> lambda argumentos: expressao

'''


