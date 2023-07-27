print("EXERCÍCIO - SEÇÃO 7")

# s7q13

'''
Faça um programa que leia uma lista de 10 posições e verifique se existem valores iguais e os escreva na tela.
'''

lista = [1, 2, 3, 4, 5, 2, 1, 3]
repetidos = []
quantas_vezes_repetiu = 1

#for i in range(10):
#    e = input("Adicione um item: ")
#    lista.append(e)

for item in lista:
    quantas_vezes_repetiu = lista.count(item)
    if quantas_vezes_repetiu > 1 and not item in repetidos:
        repetidos.append(item)
        print(f"Este {item} repetiu {quantas_vezes_repetiu}")


lista = [1, 2, 3, 4 ,5 , 2, 1, 3]
repetidos = []
quantas_vezes_repetiu = 1
print("Metodo 2" , lista)

for item in lista:
    #Pega sempre o primeiro item.
    item = lista.pop(0)
    #verifica se ta repetido
    if item in lista and not item in repetidos:
        repetidos.append(item)
        #conta quantos repetidos tem
        for item_repetido in repetidos:
            if item == item_repetido:
                quantas_vezes_repetiu += 1

        print(f"Este {item} repetiu {quantas_vezes_repetiu}")
        #Reseta para contar
        quantas_vezes_repetiu = 1
