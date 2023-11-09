print("ARGS E KWARGS")

'''
 O *args é um parâmetro, como outro qualquer,. Isso significa que você poderá chamar de qualquer coisa, DESDE QUE COMECE COM ASTERÍSICO.

ex.: *xis, *novela, *caudia, *sabonete...

O parâmetro *args utilizado em uma função, coloca valores extras informados como entrada em uma tupla. Então, desde de já lembre-se que tuplas são imutáveis.

'''

# *ARGS EXEMPLO

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 5))         OUTPUT: TypeError
# print(soma_todos_numeros(4, 5, 6, 9))   OUTPUT: TypeError

'''
Isso ocore porque passou menos/mais argumentos do que a quantidade de parâmetros que tem na função. Para resolver esse problema sem ficar adicionando um parâmetro para cada argumento, usamos o *args.
'''

def soma_numeros_exemplo(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_numeros_exemplo())
print(soma_numeros_exemplo(1))
print(soma_numeros_exemplo(2, 3))
print(soma_numeros_exemplo(2, 3, 4))
print(soma_numeros_exemplo(3, 4, 5, 6))


#Por que isso acontece? Precisamos lembrar que o *args retorna uma tupla.


def oq_retorna(*args):
    print(args)

oq_retorna()                       # OUTPUT: ()
oq_retorna(1)                      # OUTPUT: (1,)
oq_retorna(1, 2, 3)                # OUTPUT: (1, 2, 3)
oq_retorna(4, 5)                   # OUTPUT: (4, 5)
oq_retorna(1, 4, 5, 7, 9, 10, 3,)  # OUTPUT: (1, 4, 5, 7, 9, 10, 3)

# PODEMOS USAR AS PROPRIEDADES QUE APRENDEMOS NA TUPLA

def soma_numeros(*args):
    return sum(args)

print(soma_numeros())             # O resultado vai ser o mesmo 
print(soma_numeros(1))            # e o código vai estar mais limpo
print(soma_numeros(2, 3))
print(soma_numeros(2, 3, 4))
print(soma_numeros(3, 4, 5, 6))

'''
Você só precisa ficar atento ao tipo de dados porque a função sum() não vai somar str, vai somar int e reais.
'''

def exemplo_2(nome, idade, *args):
    return args

'''
Quando vc for chamar a função vc tem que definir os outros parâmetros se nã vai dar TypeError
'''
def verifica_info(*args):
    if 'Claudia' in args and 'Alves' in args:
        return f'Bem-vindo {args}!'
    return 'Eu não tenho certeza de quem você é...'

print(verifica_info())
print(verifica_info(1, True, 'Claudia', 'Alves'))
print(verifica_info(1, 2, 'Claudia'))

# OBS: ele NÃO faz operações com listas
# OBS2: ele considera a lista um elemento

'''
você pode colocar arterístico para informar ao python que estamos passando como argumento uma coleção de dados. Desta forma ele saberá que precisará antes desempacotar esses dados. Exceto dicionários porque tem chave e valor, daí a forma que desempacotar vai ser diferente.
'''

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos_numeros(*numeros))  # Assim não vai ter erro

'''
**kwargs

Assim como o args, o nome dele pode ser qualquer um contato que tenha dois asterísticos (**).

ex.: **xis, **sete, *claudia, **sapato, **doido....

Este é mais um parêmetro, mas diferente do *args que colocaos valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados e transforma esses parâmetros extras em um dicionário.

'''

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(Marcos = 'verde', Júlio = 'laranja', Fagner = 'preto', Kito = 'azul', Camille = 'amarelo', Claudia= 'vermelho')

'''
Pra tentar entender o que acontece no código acima, precisamos lembrar de desempacotamento.


lista = [1, 2, 3, 4, 5]

for numero in lista:   # ele vai passar PARA o numero tudo o que estiver         
    print(numero)      # NA lista a cada loop do for

porém esse é o exemplo com listas, em DICIONÁRIOS temos CHAVE/VALOR e é preciso desempacotar ambos. Dessa forma, no código acima temos:

1- **kwargs que vai retornar um dicionário, então precisamos de chave/valor

2- PARA 'pessoa' eu vou atribuir a chave, PARA 'cor' eu vou atribuir o valor

3- .items() é uma função que serve para acessar chave/valor nos dicionários nessa sequência.

4- o .title() é a função usada para colocar a primeira letra das palavras maiúscula. No meu caso não precisou porque eu já tinha escrito tudo maiuscula


# ORDEM OBRIGATÓRIA

def aprenda_ordem(idade, nome, *args, solteiro=false, **kwargs):

1- parâmetros obrigatórios
2- *args
3- parâmetros default (não obrigatório)
4- **kwargs


'''


# DESEMPACOTAR COM **KWARGS

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome' : 'Claudia', 'sobrenome': 'Alves'}

print(mostra_nome(**nomes))  # A partir do ** desempacota


def soma_numeros(a, b, c):
   print( a + b + c)

dicionario = dict(a = 1, b = 2, c = 3)

soma_numeros(**dicionario)


'''

OBS: os nomes da chave em um dicionário devem ser o mesmo nome dos parâmetros da função

se as chavem fossem e = 1, f = 2, g = 3, ia dar TypeError

'''


   