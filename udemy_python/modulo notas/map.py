# MAP

'''
--> SINTAXE

map(função, iterável)


map() é uma função embutida que aplica uma função a todos os itens de uma entrada iterável.

OBS: Ele vai retonar um map object

Podemos converter isso para lista, tuplas...

Em resumo, temos:

função do map só recebe um parâmetro
o map recebe mais de um iterável 

'''

def quadrado(x):
    return x ** 2

lista = [0, 1, 2, 3, 4, 5]

teste1 = list(map(quadrado, lista))

print(f"Esse é o reultado de teste1: {teste1}")

teste2 = list(map(lambda x: x**2, lista))

print(f"Esse é o resultado de teste2: {teste2}")
    
teste3 = list(map(str, lista))

print(f"Esse é o resultado do teste3: {teste3}")

import math      # Isso daqui é pra importar o valor pi

def area(r):
    return math.pi * (r ** 2)

print(area(2))
print(area(5))

# FORMA COMUM

raios = [2, 3, 4, 5, 6, 7, 8]
areas = []

for r in raios:
    areas.append((area(r)))

print(areas)

# FORMA PYTHÔNICA

areas = map(area, raios)     # area é a função que definimos alí em cima
print(list(areas))

# OU 

print(list(map(lambda r: math.pi * (r**2), raios)))

# após utilizar a função map(), depois da primeira vez usada ela se destrói

# EXEMPLO DA SOFIA

'''
No Python, um dicionário é composto por pares de chave-valor. Quando usamos o método `.items()` em um dicionário, ele retorna uma sequência de tuplas, onde cada tupla contém um par chave-valor do dicionário.
'''


# Função para dobrar os valores de um dicionário
def double_value(value):
    return value * 2

# Dicionário de exemplo
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Aplicando a função para dobrar os valores do dicionário
mapped_dict = dict(map(lambda item: (item[0], double_value(item[1])), original_dict.items()))

print(mapped_dict)

'''
1. `original_dict` é o dicionário original que contém pares chave-valor.
2. `original_dict.items()` retorna uma sequência de tuplas representando cada par chave-valor do dicionário original. Por exemplo, `('a', 1)`, `('b', 2)`, `('c', 3)`.
3. O `map()` aplica a função especificada (no exemplo, é uma função lambda) a cada item da sequência resultante de `original_dict.items()`. No caso, o lambda recebe cada tupla como `item`, onde `item[0]` representa a chave e `item[1]` representa o valor.
4. A função lambda retorna uma nova tupla com a chave (`item[0]`) mantida igual e o valor dobrado (`double_value(item[1])`).
5. Por fim, `dict()` converte a sequência resultante do `map()` de volta para um dicionário, criando um novo dicionário com as chaves originais e os valores transformados (neste caso, dobrados).

O código pode ser lido como: "Pegue cada chave e valor do dicionário original (`item[0]` e `item[1]`) e, usando a função `double_value()`, retorne uma nova tupla com a chave mantida igual e o valor dobrado. Em seguida, crie um novo dicionário com essas novas tuplas."
'''


