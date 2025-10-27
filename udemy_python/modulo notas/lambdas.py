# EXPRESSÕES LAMBDAS

'''
São funções sem nome, ou seja funções anônimas. 

Toda expressão lambda reservada começa com a palavra lambda, como ela não tem nome você vai para os parâmetros de entrada e depois o retorno.


lambda x: 3 * x + 1

Criar uma variável e usar o lambda não é a forma mais uável do lambda porque isso dá pra fazer simplesmente usando o def (Isso é só uma introdução). 

podemos ter lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()

--> o .strip() remove o espaço no início e no fim da variável. Se o seu nome for composto, ele não tira o espaço durante o meio, só no início e no final da str. Isso pode ser usado para evitar erros de pessoas que não sabem digitar direito (nesse caso).

assim como def, se passarmos mais argumentos do que parâmetros, nós teremos TypeError


'''

lambda x: 3 * x + 1  # dessa forma ela não vai gerar nenhum output

ex = lambda x: 3 * x + 1

print(ex(10))

quadrado = lambda x: x**2

print(quadrado(10))



def fun_quadrada(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


resultado = fun_quadrada(2, 4, 8)  # Aqui eu defino o valor de a, b e c                                                                                                                                                                                                                                                                                                                                                                                                                              

print(resultado(4))  # Aqui e defino o valor de x