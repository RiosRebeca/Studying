print("ESPEÇO PARA TESTE")

'''
lista = [1, 2, 3, 4, 5]

for numero in lista:
    print(numero)

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome' : 'Claudia', 'sobrenome': 'Alves'}

print(mostra_nome(**nomes))


def soma_numeros(a, b, c):
   print( a + b + c)

dicionario = dict(a = 1, b = 2, c = 3)

soma_numeros(**dicionario)
'''

lista = [ input(desejo) for desejo in range(10)]

print(lista)