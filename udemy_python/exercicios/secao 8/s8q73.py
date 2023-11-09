print("EXERCÍCIO - SEÇÃO 8")

'''
Foi realizada uma pesquisa de algumas características físicas de cinco habitantes de certa região. De cada habitante foram coletados os seguintes dados:

A) sexo 
B) Cor dos olhos (A ou C)
B) Cor dos cabeçps (L, P ou C)
C) Idade.

1- Faça uma função que leia esses dados em um vetor;
2- Faça uma função que determine a média de idade das pessoas com olhos castanhos e cabelo preto;
3- Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino cujá idade está entre 18 3 35 (inclusive) e tenha, olhos azuis;
4- Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes


sex_fem = [ pessoa for pessoa in range(popu) if pessoa == 'F' or pessoa == 'f']
sex_mas = [pessoa for pessoa in range(popu) if pessoa == 'M' or pessoa == 'm']

'''

popu = int(input("INSIRA A QUANTIDADE DE PARTICIPANTES: "))

info_popu = []

for i in range(popu):
    pessoa = {}
    pessoa['sexo'] = input(f"{i + 1} INSIRA O SEXO: ")
    pessoa['olhos'] = input(f'{i +1} INSIRA A COR DOS OLHOS: ')
    pessoa['cabelo'] = input(f'{i +1} INSIRA A COR DOS CABELOS: ')
    pessoa['idade'] = input(f'{i +1} INSIRA A IDADE: ')
    info_popu.append(pessoa)                                      # aqui ele faz uma lista com 2 dict

print(info_popu)







