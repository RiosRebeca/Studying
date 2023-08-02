print("EXERCÍCIO - SEÇÃO 7")

# s7q23

'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Montre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
'''

info_alunos = int(input("Insira a quantidade de alunos á serem cadastrados: "))

alunos = []
alturas = []

for x in range(info_alunos):
    n_cadastro = int(input(f"Insira o número de cadastro {x + 1}: "))
    nome = input(f"Insira o nome do aluno { x + 1}: ")
    altura = input(f"Insira a altura (em metros) do aluno {x + 1}: ")
    alturas.append(altura)
    aluno = {"Número de Cadastro": n_cadastro, "Aluno": nome, "Altura": altura}
    alunos.append(aluno)
    # Desse jeito eu adicione dicionários dentro de uma lista

print(alunos) 


print(max(alturas))
print(min(alturas))

