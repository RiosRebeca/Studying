print("RECAPITULANDO PYTHON")

# FUNÇÕES BÁSICAS

'''
* dir - USADO PARA LISTAR TODOS OS NOMES OU ATRIBUTOS DENTRO DE UM OBJETO. 
      A FUNÇÃO dir() VÊM DE "DIRETÓRIO" QUE EM INFORMÁTICA SIGNIFICA:    subdivisão de um disco ou de outro meio de armazenamento capaz de conter arquivos.

--> Exemplo usando dir():

dir()                  # OUTPUT: Lista os nomes no escopo atual

--> Exemplo no conseole

PS C:\Users\eurek\Documents\Studying\udemy_python> dir

                       # OUTPUT:


    Diretório: C:\Users\eurek\Documents\Studying\udemy_python


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        12/07/2023     15:30                exercicios
d-----        04/08/2023     11:08                modulo notas
-a----        10/10/2023     13:48             29 RESUMO.py

--> Exemplo 2 no console 

>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


* help - A FUNÇÃO help() FORNECE INFORMAÇÕES DE AJUDA 

--> Exemplo usando help()

help(len)        # OUTPUT: Exibe informações de ajuda sobre a função  			   len()

--> Exemplo no console 

>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

BASICAMENTE ELE O help() VAI FALAR PARA QUE SERVE A FUNÇÃO, MÓDULO, CLASSE ETC.

# STRINGS, INTEIROS E FLOATS

str - formada usando ' ', '' '', " ", """ """. Elas são imutáveis     depois de criadas, podemos INDEXAR [start:stop:step] e CONCATENAR (usando + ou +=)

--> OPERAÇÕES COM STR

upper(), lower(), split(), replace()....

* upper() - CONVERTE OS CARACTERES PARA MAIÚSCULA 
* lower() - CONVERTE OS CARACTERES PARA MINÚSCULA

texto = "Olá, Mundo!"

maiusculas = texto.upper()
minusculas = texto.lower()

print(maiusculas)  # OUTPUT: "OLÁ, MUNDO!"
print(minusculas)  # OUTPUT: "olá, mundo!"

* strip - REMOVE OS ESPAÇOS EM BRANCOS DO INÍCIO E DO FINAL DA STR 

texto = "   Python   "

sem_espacos = texto.strip()

print(sem_espacos)  # OUTPUT:: "Python"

* split - DIVE UMA STRING EM UMA LISTA DE SUBSTRINGS COM BASE EM UM CARACTERE DELIMITADOR

frase = "Python é uma linguagem de programação"

palavras = frase.split()                       # Dividir por espaços em branco (padrão)
print(palavras)                                # OUTPUT: ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

frase_csv = "maçã,banana,uva,laranja"

itens = frase_csv.split(',')                   # Dividir por vírgulas
print(itens)                                   # OUTPUT: ['maçã', 'banana', 'uva', 'laranja']

* replace - SUBSTITUI TODAS AS OCORRÊNCIAS DE UMA SUBSTRING POR OUTRA EM UMA STRING

texto = "Python é uma linguagem de programação Python"

novo_texto = texto.replace("Python", "Java")

print(novo_texto)                             # OUTPUT: "Java é uma linguagem de programação Java"

* join - CONCATENA ELEMENTOS DE UMA LISTA EM UMA ÚNICA STR, USANDO A STR ORIGINAL COMO DELIMITADOR 

frutas = ["maçã", "banana", "uva", "laranja"]

frutas_str = ", ".join(frutas)

print(frutas_str)                             # OUTPUT: "maçã, banana, uva, laranja"


--> OPERAÇÕES COM INTEIROS

* Matemática básica 

a = 5
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto_divisao = a % b
potencia = a ** b

print(soma)           # OUTPUT: 8
print(subtracao)      # OUTPUT: 2
print(multiplicacao)  # OUTPUT: 15
print(divisao)        # OUTPUT: 1.6666666666666667
print(resto_divisao)  # OUTPUT: 2
print(potencia)       # OUTPUT: 125

* CONVERSÃO DE str EM int

numero_str = "42"
numero_int = int(numero_str)

print(numero_int)     # OUTPUT: 42

* FUNÇÕES MATEMÁTICAS

import math

raiz_quadrada = math.sqrt(16)
valor_absoluto = abs(-7)
arredonda_para_cima = math.ceil(4.1)
arredonda_para_baixo = math.floor(4.9)

print(raiz_quadrada)        # OUTPUT: 4.0
print(valor_absoluto)       # OUTPUT: 7
print(arredonda_para_cima)  # OUTPUT: 5
print(arredonda_para_baixo) # OUTPUT: 4

--> FLOAT 
idem de int. (...)


# ESTRUTURA DE LÓGICA E CONDICIONAIS

--> Exemplo usando if, elif e else:

idade = intput("Insira sua idade: ")

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem 18 anos.")
else:
    print("Você é maior de idade.")

--> Exemplo OR, AND, NOT

* Quando usamos o "or" (ou), caso uma das afirmativas sejam verdadeiras ele irá considerar tudo como verdade. Ex.:

True or True --> True    False or True --> True
True or False --> True   False or False --> False

Das 4 possibilidades possíveis, 3 são consideradas verdadeiras. Vejamos o exemplo abaixo:


frutas = int(input("Quantas frutas você tem?"))
if frutas > 10 or  frutas <= 50:
    print(True)
else:
    print(False)

* Quando usamos o "and" (e) ambas as alternativas devem ser verdadeiras para considerar como True. EX.:

True and True --> True    False and True --> False
True and False --> False  False and False --> False

Das 4 possibilidades possíveis, 3 são consideradas falsas. Vejamos como o mesmo exemplo:


frutas = int(input("Quantas frutas você tem?"))
if frutas > 10 and  frutas <= 50:
    print(True)
else:
    print(False)


Quando frutas = 100, o ex.1 printa "True" porque 100 é maior que 10, então a primeira condição é verdadeira, embora a segunda seja falsa já que 100 não é igual e nem menor que 50. Já no ex.2, o print sai "False" porque 100 é maior que 10, mas não é igual e nem menor que 50. Como as duas condições não foram atendidas, então ele printa "False".


REVISANDO FUNÇÕES IMPORTANTES DENTRO DA CLASSE STR

nome = "Pamella Negromonte"
print(nome)
print(nome.split())         # Transforma em uma lista de str ['Pamella', 'Negromonte']
print(len(nome))            
print(nome[0:7])            # output: ele vai escrever o nome "Pamella" (start, stop, step)
print(nome[8:18])           # output: "Negromonte" porque start no 8, stop 18 (um antes).
print(nome.upper())         # output: PAMELLA NEGROMONTE
print(nome.lower())         # output: pamella negromonte








