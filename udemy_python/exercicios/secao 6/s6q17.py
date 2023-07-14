print("EXERCÍCIO - SEÇÃO 6")

# s6q17

'''
calcular a soma dos n primeiros números
'''

n = input("Insira um número: ")
soma = 0

for i in n:
    soma += int(i)
print(soma)  

'''
ERRADO

n = int(input("Insira um número: "))
soma = 0 

for i in n:
    soma += i
print(soma)

--> O errado aqui é que "for" não percorre int, ele percorre listas, dicionários e dupla.
--> Nesse caso, para realizar a soma eu devo transformar em int depois que ele percorrer os elementos da str.

    
    