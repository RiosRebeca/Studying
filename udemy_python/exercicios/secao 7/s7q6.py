print("EXERCÍCIOS - SEÇÃO 7")

# s7q6

'''
Faça um programa que receba do usuário um vetor com dez posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.
'''

n_vezes = []
cesta = []


for posicao in range(11):
    if n_vezes != 10:
        posicao = int(input("Digite a posição: "))
        cesta.append(posicao)

cesta.sort()
print(cesta)
print(f' O menor número é: {cesta[0]}')
print(f'O maior número é: {cesta[9]}')    

'''
--> A primeira variável é para parar o loop (não testei de outra forma);
--> A segunda variável é para armazenar os resultados fornecidos pelo usuário;
--> Usei o "for" porque eu quero que o programa percorra os elementos contidos dentro da variável e limitei a quantidade de loop ao dez vezes quando coloquei range(11);
--> Estabeleci uma condição para que, cada vez que o loop rodasse, add a informação do usuário (armazenado na posicao) na cesta;
--> usei o .sort() para colocar na sequência e printei a menor e maior posição.
'''   