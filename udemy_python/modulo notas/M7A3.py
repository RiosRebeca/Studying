print("MÓDULO 7 - DICIONÁRIOS")

'''

Dicionários - permite armazenatr e organizar informações, de forma associativa. Ele é representada por chaves {}. Chave/valor são separados por dois pontos (:) e cada chave/valor é separado um do outro usando vírgula.

ex.:
'''

# Forma MAIS COMUM de representar um dicionário

paises = { "BR": "Brasil", "EUA": "Estados Unidos", "CAN": "Canadá", "TH": "Tailândia"}

# Para ACESSAR o valor

print(paises["BR"])   # Output: Brasil
print(paises["TH"])   # Output: Tailândia

'''
Nessa forma de acessar, caso você digite uma chave inexistente, ele irá dar KeyError porque essa chave não ira existir. Para que não ocorra isso, existe outra forma de acessar os valores usando a chave.
'''

print(paises.get("CAN"))   # Output: Canadá
print(paises.get("EUA"))   # Output: Estados Unidos

'''
Nessa forma, caso você digite uma chave que não tenha no dicionário, ele não irá responder com KeuError, ele irá retornar None.

--> None é um valor especial que representa ausência de valor.
--> É usado para indicar que uma variável ou  objeto não possui valor atribuído ou não foi inicializado.

livros = {}

num_livros = int(input("Quantos livros você deseja cadastrar? "))

for i in range(n_livros):
    titulo = input(f'Digite o título do livro {i + 1}: ')
    autor = input(f'Digite o nome do autor do livro {i + 1}: ')

livros[i + 1] = {"Título": titulo, "Autor": autor}

print("\n Livros cadastrados: ")
for num_livro, info in livros.item():
    print(f"\nLivro {num_livro}: ")
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

'''

# ADICIONAR elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

receita['abr'] = 350         # Forma 1

print(receita)

novo_dado = {'mai':500} 

receita.update(novo_dado)    # Forma 2
print(receita)

# ATUALIZANDO dados em um dicionário

receita['mai'] = 550     # receita.update({'mai':600})
print(receita)

'''
--> A forma de adicionar elementos ou atualizar dados em um dicionário é a mesma.
--> Em um dicionário, não podemos ter chaves repetidas. Se você passar um valor pra chave que já existe, ele vai sobreescrever os valores, substituindo o antigo.
'''

# REMOVER dados de um dicionário

receita2 = {'jan': 100, 'fev': 120, 'mar': 300}

receita.pop('mar')   # remove o último elemento da lista
print(receita)

# OBS: aqui precisamos SEMPRE informar a chave, e caso não encontrada, retorna KeyError
# OBS: ao revorvermos o objeto, o valor dele é sempre retornado (usando o pop)

del receita['fev']        # forma 2: del de deletar
print(receita)

'''
Imagine a seguinte situação:

carrinho
    produto 1:
        - nome:
        - quantidade:
        - preço:
    produto 2:
        - nome:
        - quantidade:
        - preço:
'''

# Usar lista (forma 1)

carrinho = []

produto1 = ['Playstation 4', 1, 5000]
produto2 = [God of War 4', 1, 150]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

'''
--> teríamos que saber qual o índice de cada informação no produto
'''

# Usar tupla (forma 2)

produto3 = ( 'Playstation 4', 1, 2300.00)
produto4 = (' U scape', 1, 30.00)

carrinho = (produto3, produto4)

print(carrinho)

# Usar um dicionário (forma 3)

protudo5 = {'nome': 'Playstation", 'quantidade': 1, preço:'2000'}
produto6 = {'nome': 'X-box', 'quantidade': 1, 'preço': 3000}

carrinho.append(produto5)
carrinho.append(produto6)

print(carrinho)

'''
O que acontece, é que nos outras coleções (lista, tupla) só vamos ter a informação bruta, já no dicionário o output vai sair chave/valor facilitando a identificação.
Dessa forma, facilmente add ou remv produtos no carrinho e podemos ter certeza sobre cada informação.
''

# MÉTODOS de dicionários

d = dict(a=1, b=2, c=3)

d.clear()  # Limpar o dicionário (zerar dados)

novo = d.copy()   # COPIAR os valores de um dicionário p/ outro
print(novo)

novo['d'] = 4 

print(d)
print(novo)


novo = d    
print(novo)
novo['d'] = 4     # Os dois vão ser alterados shallow copy

print(d)
print(novo)


