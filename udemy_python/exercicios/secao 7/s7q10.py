print("EXERCÍCIO - SEÇÃO 7")

# s7q10

'''
Faça um porgrama para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
---> eu quero pegar os valores da lista e tirar a média
---> eu vou somar os elementos da lista

lista = [1, 2, 3, 4, 5]
soma = 0

for elmento in lista:
    soma+= elemento
-------------------------------

soma = sum(lista)

-------------------------------

--> É importante lembrar que o programa é lido de baixo para cima.
--> só realize as operações quando os dados das variáveis estiverem devidamente preenchidos

'''

planilha = []

for notas in range(15):
    nota = int(input("Insira o valor da nota: "))
    planilha.append(nota)

nota_dos_alunos = sum(planilha)
media_geral = nota_dos_alunos / 15

print(planilha)
print(media_geral)

