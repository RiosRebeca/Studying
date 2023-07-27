print("EXERCÍCIO - SEÇÃO 7")

# s7q13

'''
Faça um programa que leia uma lista de 10 posições e verifique se existem valores iguais e os escreva na tela.
'''

lista = []
repetidos = []

for i in range(10):
    e = input("Adicione um item: ")
    lista.append(e)

for item in lista:
    quantas_vezes_repetiu = lista.count(item)
    if quantas_vezes_repetiu > 1 and not item in repetidos:
        repetidos.append(item)
        print(f"Este {item} repetiu {quantas_vezes_repetiu}")