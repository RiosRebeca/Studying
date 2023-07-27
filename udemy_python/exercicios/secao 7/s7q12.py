print("EXERCÍCIO - SEÇÃO 7")

# s7q12

'''
Faça um programa para ler 5 valores e, em seguida, mostrar todos os valores lida juntamente com o maior, o menor e a média dos valores.
'''

valores = []

for ler in range(5):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

print(valores)

media = sum(valores) / 5
print(min(valores))
print(max(valores))
print(media)

