print("SEÇÃO 7 - MODULO COLLECTIONS")

'''
Módulo Collections - Counter

Collections é um múdulo do python que permite fazer mudanças interativas nas coleções que já vimos.

collections --> high-performance container datatypes

counter seria algo como "contador" em português. 

Ele recebe um interável como parâmetro e cria um objeto tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento.
'''

# Utilizando o counter

from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# OBS: podemos usar qualquer iteravel, aqui colocamos inteiros na lista, mas poderíamos usar outros.

res = Counter(lista)

print(type(res))         # Output: <class 'collections.Counter'>

print(res)               # Output: Counter({2: 6, 1: 5, 3: 5, 5: 5, 4: 4, 45: 2, 66: 2, 43: 1, 34: 1}) encontrou 6x o número 2, 5x o 3...
                         # Aqui nós temos o valor/quantidade de vezes

'''
--> Veja que para cada elemento da lista o counter criou uma chave e colocou como valor a quantidade de ocorrências

--> Poderia ser uma tupla, um dicionário, um str...contanto que se passe valores.

'''

from collections import Counter

print(Counter('Pamella Micaelly"))     # Output: Counter({'l': 4, 'a': 3, 'e': 2, 'P': 1, 'm': 1, ' ': 1, 'M': 1, 'i': 1, 'c': 1, 'y': 1}) 

                                       # Ele colocou como chave os dados fornecidos e coloca como valor a quantidade de vezes que ele se repete

texto = """Ando por aí querendo te encontrar//Em cada esquina, paro em cada olhar//Deixo a tristeza e trago a esperança em seu lugar//Que o nosso amor pra sempre viva, minha dádiva//Quero poder jurar que essa paixão jamais será//Palavras apenas//Palavras pequenas//Palavras, momento//Palavras, palavras//Palavras, palavras//Palavras ao vento """

print(Counter(texto))
Counter({'a': 54, ' ': 43, 'r': 26, 'e': 26, 's': 21, '/': 20, 'o': 19, 'n': 12, 'v': 12, 'p': 11, 'l': 10, 'u': 9, 'm': 9, 'i': 8, 'd': 7, 't': 7, 'P': 6, ',': 5, 'q': 4, 'c': 3, 'h': 2, 'x': 2, 'g': 2, 'Q': 2, 'á': 2, 'j': 2, 'A': 1, 'í': 1, 'E': 1, 'D': 1, 'z': 1, 'ç': 1, 'ã': 1})

# VERDADEIRO USO QUE ELE QUERIA MOSTRAR	

palavras = texto.split()    # Aqui usamos o .split() p/ separar as palavras da str

print(palavras)

['Ando', 'por', 'aí', 'querendo', 'te', 'encontrar//Em', 'cada', 'esquina,', 'paro', 'em', 'cada', 'olhar//Deixo', 'a', 'tristeza', 'e', 'trago', 'a', 'esperança', 'em', 'seu', 'lugar//Que', 'o', 'nosso', 'amor', 'pra', 'sempre', 'viva,', 'minha', 'dádiva//Quero', 'poder', 'jurar', 'que', 'essa', 'paixão', 'jamais', 'será//Palavras', 'apenas//Palavras', 'pequenas//Palavras,', 'momento//Palavras,', 'palavras//Palavras,', 'palavras//Palavras', 'ao', 'vento']

res = Counter(palavras)
print(res)

Counter({'cada': 2, 'em': 2, 'a': 2, 'Ando': 1, 'por': 1, 'aí': 1, 'querendo': 1, 'te': 1, 'encontrar//Em': 1, 'esquina,': 1, 'paro': 1, 'olhar//Deixo': 1, 'tristeza': 1, 'e': 1, 'trago': 1, 'esperança': 1, 'seu': 1, 'lugar//Que': 1, 'o': 1, 'nosso': 1, 'amor': 1, 'pra': 1, 'sempre': 1, 'viva,': 1, 'minha': 1, 'dádiva//Quero': 1, 'poder': 1, 'jurar': 1, 'que': 1, 'essa': 1, 'paixão': 1, 'jamais': 1, 'será//Palavras': 1, 'apenas//Palavras': 1, 'pequenas//Palavras,': 1, 'momento//Palavras,': 1, 'palavras//Palavras,': 1, 'palavras//Palavras': 1, 'ao': 1, 'vento': 1})

print(res.most_common(3))                  # Para saber AS MAIS RECORRENTES

[('cada', 2), ('em', 2), ('a', 2)]