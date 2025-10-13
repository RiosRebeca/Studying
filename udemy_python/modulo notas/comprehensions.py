print("COMPREHENSIONS em PYTHON")

'''
É uma forma concisa de escrever listas, dicionários e sets. Você faz o código em uma linha só.
'''

squares = []                 # Crio uma lista onde vou add elementos

for x in range(10):     
    squares.append(x ** 2) 
                             # O loop vai rodar 10 vezes e add de 1-10 na 
                             # lista, além disso vai pegar o x e elevar 2
# OUTRA FORMA DE ESCREVER

squares = [x ** 2 for x in range(10)]

# A lista é igual a x elevado a 2, para x em range 10
# Quer dizer que eu vou definir como a lista vai ser montada e depois eu
# defino o meu 'x'

# MEU EXEMPLO

lista = [ input(desejo) for desejo in range(1, 1, 11)]

print(lista)

'''

List Comprehension - podemos gerar novas listas com dados processados a partir de outro iterável.

# SINTAXE

lista = [ dado for dado in iterável]

Para cada dado nessa coleção de dados, coloque esse dado na minha lista.
Você pode fazer o que quiser no dado, como foi mostrado no exemplo acima.
'''



numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


'''
Para entebder o que está acontecendo, devemos dividir a expressão em duas partes:

1- for numero in numeros
2- numero * 10

primeiro eu digo o que eu quero, depois eu digo de onde vem.

'''

# DICTIONARY COMPREHENSION

'''

--> SINTAXE

dicionario = {chave: valor for valor in iterável}


'''


squares = {x: x*x for x in range(1, 6)} 

# OUTPUT: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {x: x*x for x in range(1, 6) if x % 2 == 0}

# OUTPUT: {2: 4, 4: 16}


numeros = [1, 2, 3, 4, 5, 6]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)










