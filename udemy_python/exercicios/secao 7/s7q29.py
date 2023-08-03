print("EXERCÍCIO - SEÇÃO 7")

# s7q29

'''
Faça um programa que leia dois vetores de 10 elements. Crie um vetor que seja a interseção entre os dois vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Não deve conter números repetidos.
'''

alunos_etecm = {'Rebeca', 'Victor', 'Fagner', 'Sergio', 'Ana', 'Mateus', 'Rafael', 'André', 'Jessica', 'Maria'}
alunos_cemo = {'Rebeca', 'Marcos Gabriel', 'Maria', 'Mateus', 'Pamella', 'Paloma', 'Dennis', 'Pamily', 'Samara', 'Wagner'}

alunos = alunos_etecm.intersection(alunos_cemo)

print(f'O slaunos do ETECM são: {alunos_etecm}')
print(f'Os alunos do CEMO são: {alunos_cemo}')
print(f'Os alunos de ambas as escolas são:{alunos}')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

alunos_etecm = ['Rebeca', 'Victor', 'Fagner', 'Sergio', 'Ana', 'Mateus', 'Rafael', 'André', 'Jessica', 'Maria']
alunos_cemo = ['Rebeca', 'Marcos Gabriel', 'Maria', 'Mateus', 'Pamella', 'Paloma', 'Dennis', 'Pamily', 'Samara', 'Wagner']


aluno = []

for i in alunos_etecm:
    if i in alunos_cemo:                 
        aluno.append(i)

print(aluno)
    
# Se eu quiser verificar se algo está dentro de uma lista, eu uso o 'if' e o 'in' (dentro)