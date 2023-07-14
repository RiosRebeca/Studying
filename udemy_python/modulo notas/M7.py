print("SEÇÃO 7 - LISTAS")

'''
As listas são usadas para armazenar  uma coleção de elementos. Em python, elas são mútaveis e podem armazenar diferentes classes (int,str, boolean, etc.)
'''

minha_lista = [1, 2, 3, 4, 5]

'''
Podemos acessar os elemntos da lista usando índices. É importante lembrar que o primeiro elemento da lista é contado na posição zero e assim por diante.
'''

minha_lista = [1, 2, 3, 4, 5]

print(minha_lista[0])  # Output: 1
print(minha_lista[2])  # Output: 3

type([])               # Isso já é uma lista com elementos vazios

lista_a = [ 1, 99, 34, 100, 79, 42, 17, 58 ]
lista_b = ['P', 'a', 'm', 'e', 'l', 'l', 'M', 'i', 'c', 'e', 'l', 'l', 'y']
lista_c = []
lista_d = list(range(16))
lista_e = ['Pamella Micaelly']

# Podemos verificar se um elemento está dentro da lista

if 42 in lista_a:
    print("Encontrei o número")
else:
    print("Não encontrei o número")

# Podemos ordenar uma lista usando .sort()

lista_a.sort()
print(lista_a)

lista_b.sort()
print(lista_b)

# Podemos contar números de ocorrência de um elemento na lista

print(lista_a.count(1))
print(lista_e.count('l'))

# Podemos adicionar elemento, utilizando a função .append () 

print(lista_a)
lista_a.append(29)  # ele só add um por vez
print(lista_a)

'''
Podemos adicionar qualquer tipo de alimento na lista, inclusive outra lista.
'''

lista_a.append([29,  13, 24])  
print(lista_a)


# Para add elementos, usamos a função .extend() 


print(lista_e)
lista_e.extend(['e', 'Rebeca Keylla'])
print(lista_e)

minha_lista = [1, 2, 3]
outra_lista = [4, 5, 6]

minha_lista.extend(outra_lista)
print(minha_lista)  # Output: [1, 2, 3, 4, 5, 6]
 
# Podemos adicionar elementos em posições ESPECÍFICAS da lista usando o .insert(posição, argumento)

minha_lista = [1, 2, 3, 4]

minha_lista.insert(1, 5)
print(minha_lista)  # Output: [1, 5, 2, 3, 4]

# Podemos juntar duas listas usando o '+' sem precisar o .extend()

lista_b = lista_b + lista_e

# Podemos inverter uma lista .reverse()

minha_lista.reverse()
print(minha_lista)

lista_b([::-1])

# Remover o último elemento de uma lista


minha_lista = [1, 2, 3, 4]
minha_lista.remove(2)
print(minha_lista)  # Output: [1, 3, 4]

minha_lista.pop(0)
print(minha_lista)  # Output: [3, 4]

'''
no .pop() podemos colocar qual a posição do elemento que queremos remover.
'''









