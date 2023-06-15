print("STRING e INTEIRO")

# a é uma string, e string não realizam operações matemáticas
a = "1+1"

#b é um inteiro, inteiros são números que realizam operações matemáticas
b = 1+1

#Aqui utilizamos uma função built-in chamada type(), ela nos retorna em string o
#tipo de variável, sendo útil para sabermos como lidar com determinadas situações

print(type(a))
print(type(b))
s
# Strings não podem ser somadas a inteiros sem antes serem convertidas
# para converter algo em string, precisamos usar a built-in function str()

print(a + " = " + str(b))

#Nesse exemplo, nós convertermos um inteiro para string, o que permitiu
#concatenar as string e somá-las. 

resposta=input("Vamos praticar?")

#----------------------------------------------------------------------------

#No nosso próximo exemplo faremos o inverso, iremos converter string em inteiro
#para realizar operações matemáticas numéricas em geral. Primeiro vamos definir
#nossas variáveis

cestas = 1
macas = 5

#Agora vamos estabelecer um cálculo de cestas para maçãs que nos dirá quantas #maçãs temos

numerodemacas = cestas * macas

"""Acima nós utilizamos uma operação matemática para calcular o número de maçãs
baseado no numero de cestas. Observe que o número será sempre 5 pois não temos 
alterações nas variáveis."""

#Para isso, vamos pedir ao usuário que conte quantas cestas ele consegue imaginar.

cestas = input("Quantas cestas de macas você consegue imaginar?\n")

#Acima utilizamos uma outra biut-in function que permite interagir com o usuário
#recebendo pela linha comando chamada stdin o valor e retornando em string, que
#fica armazenado nesse caso na função cestas.

#Para validar veja que tipo de variável é a vaiável cestas. 

print(type(cestas))

a=50
b=12
soma=a+b

soma=input("qual o valor da soma de 50+12?")
print("Você respondeu"+int(soma))