print("EXERCÍCIO - SEÇÃO 6")

# s6q18


'''
Escreva um algorítimo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos devem ser fornecidos pelo usuário.
'''

quantidade = int(input("Digite o número de vezes: "))
n_maximo = 0
quantia_de_n_maximo = 1 #sempre vai haver um numero maximo por isso começamos a contar por 1

for vezes in range(quantidade):
    numero = int(input("Insira um número: "))
    #print("Antes: ", quantia_de_n_maximo, n_maximo, numero, n_maximo == numero)
    if n_maximo == numero: # e importante checar antes de definir 
        quantia_de_n_maximo += 1
    if numero > n_maximo:
        quantia_de_n_maximo = 1 # Redefinir a contagem para cada numero maximo
        n_maximo = numero
    #print(quantia_de_n_maximo, n_maximo, numero, n_maximo == numero)

print(f"O maior numero foi {n_maximo} e ele foi atingido {quantia_de_n_maximo} vezes")

    

#print(a maior nota)
    





'''
n = "Quantas notas tiveram ? (Quantos Alunos ?)"
"Quais foram as notas em ordem ?" (Perguntar n vezes)
"Printar a quantia de aluno que alcançaram a maior nota" 
'''