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

--> Para verificar se há ELEMENTOS REPETIDOS

frutas = ['maçã', 'banana', 'laranja', 'maçã', 'uva', 'maçã']
ocorrencias = frutas.count('maçã')
print(ocorrencias)  # Saída: 3

--> O count() é um método que tem como objeivo contar o número de ocorrências de um determinado elemento na sequência.

# Podemos adicionar elemento, utilizando a função .append() 

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
 
# Podemos adicionar elementos em POSIÇÕES ESPECÍFICAS da lista usando o .insert(posição, argumento)

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

# Converter uma str para uma lista

lista_1 = "Sofia é muito inteligente"
lista_1 = Lista_1.split()   # Output:   lista_1 = "Sofia", "é", "muito", "inteligente"

'''
Por padrão, o separador das str é uma vírgula, mas podemos adicionar outro separador se espercificamos assim: ('')
'''

lista_2 = "Eu quero aprender python"
lista_2 = lista_2.split(',')

# Converter uma lista para uma str

lista_3 = ['Um', 'dois', 'três', 'indiozinhos']
musica = ' '.join(lista_3)
print(musica)                  #Output: Um dois três indiozinhos

'''
estamos falando: pega a lista_3, coloca espaço entre cada elemento e transforma em uma lista. Podemos adicionar mais coisas antes dentro dos ('').join, como caractéres, letras, listas...o importante é usar a lógica.
'''

# Iterando sobre listas 

lista_4 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elemento in lista_4:
    print(elemento)

#output:
'''
1
2
3
4
5
6
7
8
9
10

--> Em programação, iteirar significa passar por cada elemento de uma coleção (lista, str, tupla, dicionário etc.) e realizar uma ação em cada elemento.
--> Não dá para add um valor int a lista sem antes tranformar, por isso usamos a função range(len(lista)).
--> Aqui você diz que quer len() o COMPRIMENTO da lista e ele VAI RETORNAR UM INT.
--> O range() é usado para você saber o alcance de algo, nesse exemplo lista é o STOP
'''

# Iterar usando o while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um elemento na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Fazemos acesso aos elementos de forma indexada

roupas = [camisa, short, blusa, moletom, calça, bota, sapato, sandália]
print(roupas[0])
print(roupas[4])

ele vai printar camisa e calça porque camisa está na posição 0 e calça na posição 4. 

'''
.index()

--> slicing [ start, stop, step] que nem o range

'''

lista = ["maçã", "banana", "laranja", "uva"]

for indice, elemento in enumerate(lista):
    print(f"O elemento {elemento} está na posição {indice}")


# Invertendo valores em uma lista 

nomes = [ 'Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

#output: ['University', 'Geek']

# Para saber o valor máximo e o valor mínimo

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(min(a))     # output: 1
pint(max(a))      # output: 9






