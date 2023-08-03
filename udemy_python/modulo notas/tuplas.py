print("Aula de Tuplas")


'''
 Tuplas ão bastante parecidas com listas. Existem, basicamente duas diferenças:

 1- As tuplas são representada por parênteses ()
 2- As uplas são imutáveis, ao se criar uma tupla ela não muda. Toda operação em tupla gera uma nova tupla.

OBS: as tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))      # output: <class 'tuple'>

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))      # output: <class 'tuple'>

OBS2: Tuplas com 1 elemento

tupla3= (4)
print(type(tupla3))      # output: <class 'int'>

Mesmo que a representação dele esteja em (), não é uma tupla.

t4 = (4,)
print(type(t4))          # output: <class 'tuple'>

AS TUPLAS SÃO DEFINIDAS PELAS VÍRGULAS (,) E NÃO PELO USO DO PARÊNTESIS.

t5 = 1 2 3 4 5

SyntaxError: invalid syntax

# Podemos gerar uma Tupla com range 

tupla = tuple(range(11))
print(type(tupla))
print(tupla)

# Desempacotamente de tupla

tupla = "Rebeca Keylla", "Pamella MIcaelly")

escola, curso = tupla        

--> escola e curso vão receber o valor da tupla, respectivamente.
--> Tem que colocar o mesmo valor pra mesma variável se não vai dar erro. Não pode ter três valores e duas variáveis, por exemplo.

# Métodos para ADD e REMOÇÃO de elementos nas duplas NÃO EXISTEM dado ao fato das tuplas serem imutáveis.

tem como usar as funções som(), max() e min() nas tuplas também. 

# CONCATENAÇÃO de tuplas

t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(t1 + t2)   # output: (1, 2, 3, 4, 5, 6)

print(t1)        # output: (1, 2, 3)
print(t2)        # output: (4, 5, 6)

--> elas voltam a ter os mesmos valores porque elas são imutáveis, mas podemos sobre escrever os seus valores porque ela não é uma constante.


# Verificar se um elemento está na tupla

t = (1, 2, 3)

print(3 in t)

# INTERANDO sobre uma tupla

tupla = 5, 6, 7, 4

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# CONTANDO elemntos dentro de uma tupla

tupla = ( "a", "b", "c", "d", "e", "a", "c")

print(tupla.count("a"))

# DICAS NA UTILIZAÇÃO DE TUPLAS

--> Devemos usar tupls SEMPRE que não precisarmos modificar os dados contidos em uma coleção.

ex.: meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')

--> Não faz sentido permitir que coleção de meses seja modificada, nem por você nem por outro programador. 

# O ACESSO usando INDICE é igual ao da lista

meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')

print(meses[7])
print(meses.index('abr'))

# POR QUE usar tuplas?

--> tuplas são mais rápidas o que listas (ex, quando você está trabalhando com ciência e dados ou inteligência artificial, isso melhora a performance. Se você está utilizando dados, você pode usar tuplas).

--> Tuplas deixa o seu código mais seguro, isso porque trabalha com elementos imutáveis traz segurança para o código. 

# Copiando uma tupla para outra 

tupla = (1, 2, 3)
print(tupla)

nova = tupla    # na tupla não temos problemas de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova) 
print(tupla)

'''