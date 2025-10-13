'''
x = int(input("DIGITE UM NÚMERO INTEIRO: "))

if x < 0:
    print("negativo")
    resp1 = "negativo"
else:
    print("positivo")
    resp1 = "positivo"

if x % 2 == 0:
    resp2 = "par"
    print("par")
else:
    resp2 = "impar"
    print("ímpar")


animais = ["gato", "coelho", "macaco", "girafa"]

animais.remove("gato")
print(animais)
print(len(animais))
print(animais.index("coelho"))
'''

notas = {"ana":[7.5, 8.0], "bruno":[1, 1] , "carlos":[1, 1], "julia": [1,2,3,4,5]}

#def incognita(x):
#    if x in notas:
#        print(f"Media do aluno {x}: {sum(notas[x])/len(notas[x])}")
#
#for aluno in notas:
#    incognita(aluno)
#
#list(map(lambda x: print(f"Media do aluno {x}: {sum(notas[x])/len(notas[x])}") if x in notas else None, notas))

aluno = input("Nome do aluno: ")
media=sum(notas[aluno])/len(notas[aluno]) if aluno in notas else "O aluno não tem media."
print(f"A Media do Aluno {aluno} é: {media}")



#def calc_media(nome:str, notas):
#    media = (notas[nome][0] + notas[nome][1])/2
#    return media 
##print((notas["ana"][0] + notas["ana"][1])/2) --> raciocínio criado
#
#print(calc_media("ana", notas))
   
