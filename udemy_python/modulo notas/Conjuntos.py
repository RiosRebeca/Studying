print("SEÇÃO 7 - CONJUNTOS")

'''
Conjuntos - em qualquer linguagem de programação, estamos fazend referência a teoria dos conjuntos da metemática.

--> no python, os conjuntos são chamados de sets.
--> os sets não possuem valores duplicados
--> Não possuem valores ordenados
--> os valores não são acessados via índice, os conjuntos não são indexidados.

Os conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados. Os conjuntos (sets) são referenciados em python com chaves {}.

Dicionários vs Conjuntos (sets)

--> Dicionário tem chacve/valor, conjunto tem apenas valor.

'''

# DEFININDO CONJUNTO:

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})         # Temos valores repetidos

print(s)          # Output: {1, 2, 3, 4, 5, 6, 7}
print(type(s))    # Output: <class 'set'>

--> Os valores repetidos serão ignorados e o set será imprimido sem causar erro.

amor = set("Fagner Alves")
print(amor)

ou 

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}

print(s)
print(type(s))

# Podemos verrificar SE ESTÁ DENTRO OU NÃO

if 3 in s:
    print("Tem o número 3"
else:
    print("Não tem o número 3")

--> É importante lembrar que, além de não ter valores duplicados, não temos ordem.

lista = [99, 2, 34, 23, 12, 1, 2, 34 44, 5]
print(f"Lista: {lista} com {len(lista)} elementos")                        # Output:  Lista: [99, 2, 34, 23, 12, 1, 2, 34 44, 5] com 10 elementos

tupla = (99, 2, 34, 23, 12, 1, 2, 34, 44, 5)
print(f"Tupla: {tupla} com {len(tupla)} elementos")                        # Output: Tupla: (99, 2, 34, 23, 12, 1, 2, 34 44, 5) com 10 elementos

dicionario ={}.fromkeys([99, 2, 34, 23, 12, 1, 2, 34, 44, 5], 'dict')      # Output: Dicionário: ... com 8 elementos
print(f'Dicionário: {diocionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 12, 1, 2, 34, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')               # Output: Conjunto: {1, 2, 99, 34, 5, 12, 44, 23} com 8 elementos


--> No dionário não repete CHAVES, e como está transformando tudo em chaves, ele vai tirar ps números repetidos (2 e 34)
--> O conjunto não repete VALORES, da mesma forma, ele vai tirar os números repetidos (2 e 4) e tem a própria ordem dele
--> Listas e Tuplas aceitam valores duplicados e por isso temos 10 elementos.

Assim como todo outro conjunto python, podemos colocar todos os tipos de dados misturados em séries. Por exemplo:

s = { 1, 'b', True, 34.22, 44}
print(s)
print(type(s))                          # Output:  <Class 'set'>

# Podemos ITERAR em um set normalmente

for valor in s:
    print(valor)

# USOS interessantes do set

--> Imagine que fizemos um formulário de cadastro de visitantes em que uma feira ou museu e os visitantes informam manualemnte a cidade de ibde vieram.
--> Nós add cada cidade em uma lista python, já que em uma lista podemos add novos elementos e ter repetições.

cidades = ['Beleo Horixzonte', 'São Paulo', 'Cuiabá', 'São Paulo', 'Olinda', 'Recife', 'Buriti Alegre', 'Olinda', 'Recife', 'Macaé']
print(len(cidades))

--> Dessa forma conseguiríamos ver a quantidade de pessoas, mesmo em cidades repetidas;
--> Mas, se eu quiser saber de quantas cidades diferentes vieram essas pessoas, eu uso o set

print(len(set(cidades)))            # Output: 7

# ADICIONANDO ELEMENTOS em um conjunto

s = {1, 2, 3}
s.add(4)
print(s)                            # Output: {1, 2, 3, 4}

--> Se eu add um elemento que já tem no set, ele não vai gerar erro, apenas será ignorado.

# REMOVER ELEMENTOS em um conjunto

s.remove(3)   # isso NÃO É INDICE, informamos o valor que vai ser removido. Se fosse um str, eu colocaria str.
print(s)      # OBS: caso o valor não seja encontrado, será gerado o erro KeyError

ou 

s.discard(2)
print(s)      # Se o valor não for encontrado, nenhum erro é gerado.

# COPIANDO um conjunto

--> Deep copy

novo = s.copy()
print(novo)           # Output: {1, 2, 3}

print(s)              # Outuput: {1, 2, 3, 4}


--> São idependentes. Cria uma nova lista e copia todos os objetivosda lista original.


--> Shallow copy

novo = s
novo.add(4()

print(novo)           # Output: {1, 2, 3, 4}
print(s)              # Output: {1, 2, 3, 4}

--> os dois vão ser modificados porque (novo = s) e quando for printar novamente, as duas estarão alteradas.


# REMOVER TODOS OS ITENS de um conjunto

s.clear()
print(s)              # Output: {}

# MÉTODOS MATEMÁTICOS DE CONJUNTOS

--> Imagine que temos dois conjuntos, um  contendo estudantes do curso python e utro do curso de java.

estudantes_python = {'Marcos', 'Camille', 'Fagner', 'Pamella', 'Rebeca', 'Alex'}
estudantes_java = {'Fernando', 'Gustavo', 'Fagner', 'Rebeca', 'Keven'}

--> Veja que algunsalunos que estudam python também estudam java.
--> Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - utilizando UNION

unico1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere PIPE (|)

unicos2 = estudantes_python | estudantes_java
print(unicos2)

--> Agora precisamos gerar um conjunto de estudantes que estão em AMBOS OS CONJUNTOS

# Forma 1 - utilizando o INTERSECTION

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

--> Agora queremos gerar um conjunto de estudantes que ESTÃO EM UM, MAS NÃO ESTÃO EM OUTRO

# Forma 1 - utilizando o DIFFERENCE

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_vaja.difference(estudantes_python)
print(so_java)


# SOMA, VALOR MÁXIMO, MÍNIMO E TAMANHO

--> Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
