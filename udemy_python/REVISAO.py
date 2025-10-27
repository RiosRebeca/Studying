#REVISÃO DOS ÚLTIMOS MÓDULOS 

#def voltei():
#    return print("É muito bom estar de volta")
#
#voltei()

def diga_oi(nome):
    return f"Olá, {nome}!"

#print(diga_oi("casada"))

from random import random

def lavar_pratos():
    result = random()
    if result < 0.5:
        return "Fagner"
    return "Rebeca"

#print(f"Hoje quem lava os pratos é: " + lavar_pratos())

def professor(instituicao="Acordes", instrutor=False):
    if instituicao == "Acordes" and instrutor == True:
        nome = input("Digite seu nome:")
        return f"Seja-bem vindo(a) prof. {nome}"
    nome = input("Digite seu nome:")
    return f"Desculpe {nome}, achei que você era o prof."

#print(professor())
#print(professor(instrutor=True))
    

total = 0 # evitar var global

def conte():
    global total # Estou dizendo que peguei uma var global
    total = total + 1
    return total

#print(conte()) 
#print(conte())
#print(conte())

def soma_numeros(*args):
    print(args) # os argumentos vão para uma tupla
    return sum(args), max(args), min(args), len(args) #aceita os métodos aplicáveis às tuplas


#print(soma_numeros(0,1, 2, 3, 4,))

pessoas = ["Rebeca", "Fagner", "Sofia", "Lucas", "Mariana", "João", "Carla", "Pedro", "Ana",
    "Bruno", "Fernanda", "Rafael", "Camila", "Gustavo", "Patrícia", "Eduardo", "Larissa",
    "Felipe", "Juliana", "André", "Bianca", "Vinícius", "Paula", "Rodrigo", "Isabela"]

pessoas2 = ["Luiz", "Rogério", "Jericoacoara", "Gabrielly", "Cinderela"]

def convidados(*args):
    nome = input("Digite seu nome: ")
    if nome in args:
        return f"Bem vindo (a) {nome}"
    return "Não encontramos seu nome na lista"

#print(convidados(*pessoas)) #output: Bem-vindo (a): Rebeca
#print(convidados(*pessoas2)) #output: Não encontramos seu nome na lista

alunos_instrumentos = {
    "Ana": "Piano",
    "Bruno": "Violão",
    "Carla": "Violino",
    "Daniel": "Bateria",
    "Eduarda": "Teclado",
    "Felipe": "Guitarra",
    "Giovana": "Flauta",
    "Henrique": "Saxofone",
    "Isabela": "Violoncelo",
    "João": "Baixo",
    "Karen": "Trompete",
    "Lucas": "Percussão",
    "Mariana": "Ukulele",
    "Nathan": "Gaita",
    "Olívia": "Clarinete",
    "Pedro": "Canto",
    "Quésia": "Harpa",
    "Rafaela": "Oboé",
    "Samuel": "Acordeão",
    "Tatiane": "Bandolim",
    "Ubirajara": "Teclado",
    "Vitória": "Piano",
    "William": "Violão",
    "Xavier": "Bateria",
    "Yasmin": "Cello",
    "Zeca": "Guitarra"
}



def matricula(**kwargs):
    for aluno, instrumento in kwargs.items():
        print(f"O instrumento de {aluno} é {instrumento}")

#matricula(**alunos_instrumentos) # ele não recebe o dict direto

def aula(**kwargs):
    for aluno, instrumento in kwargs.items():
        if instrumento == "Piano" or instrumento == "Teclado":
            print(f"{aluno} irá para prof. Rebeca")
        elif instrumento == "Ukulele":
            print(f"{aluno} irá para pof. Elvis")

#aula(**alunos_instrumentos)



