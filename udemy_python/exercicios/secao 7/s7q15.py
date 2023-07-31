print("EXERCÍCIO - SEÇÃO 7")

# s7q15

'''
Faça um programa que leia um vetor de cinco posições para números reais e, depois, um código inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direita; se for 2, mostre o vetor na ordem inversa. Caso o código for diferente de 1 e 2, escreva uma mensagem informado que o código é inválido.
'''

n_reais = []

for n in range(5):
    n_escolhido = int(input("ISIRA UM NÚMERO: "))
    n_reais.append(n_escolhido)

codigo = int(input("Escolha um número de 0 á 2: "))
if codigo == 1:
    print(n_reais) 
elif codigo == 2:
    n_reais.reverse()
    print(n_reais)
elif codigo == 0:
    exit()    
else:
    print("Código inválido")
