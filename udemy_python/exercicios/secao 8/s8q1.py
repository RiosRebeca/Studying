print("EXERCÍCIOS - SEÇÃO 8")


# Crie uma função que receba um número inteiro e devolve o seu dobro

'''
def dobro(a:int):
   resultado = a * 2
   return resultado

resultado = dobro(3)
print(resultado)

'''

a = int(input("INSIRA O VALOR DE A: "))   # Aqui o usuário define 'a'

def dobro(a:int):                         # O argumento 'a' te que ser um int
    resultado = a * 2                     # Aqui é o que a função faz
    return resultado                      

print(dobro(a))

'''
Depois que a função acabar de executar sua tarefa, ela vai retornar o resultado da tarefa para dobro().

Mas a função só vai começar a fazer tudo isso caso ela seja chamada. Aqui, nós chamamos a função com o print(). - Ao chamar a função, você está dizendo ao Python para executar o código dentro dela com os valores específicos que você forneceu como argumentos. - Então se eu colocasse print(dobro(OUTRO NÚMERO)) ele ia executar o código com o valor do argunmento e bão ia mais usar o input.

'''