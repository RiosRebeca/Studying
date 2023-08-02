print("EXERCÍCIO - SEÇÃO 7")

# s7q22

'''
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por x1 * y1 + x2 * y2 ... xn* yn.
'''

lista1 = []
lista2 = []

for a in range(5):
    m = int(input("ADICIONE UM NÚMERO NA LISTA 1: "))
    lista1.append(a)

for b in range(5):
    n = int(input("ADICIONE UM NÚMERO NA LISTA 2: "))
    lista2.append(b)

produto_escalar = []

z = int(input("Adicione o limite do produto escalar: "))

if z <= len(lista1) and z <= len(lista2):  
    for c in range(z):
        x = lista1[c // 2]
        y = lista2[c // 2]
        p_escalar = ( x * y)
        produto_escalar.append(p_escalar)
else:
    print("Existem apenas 5 elementos em cada lista. Insira um número de 1 á 5.")

print("Produto escalar: ", produto_escalar)
    
'''

#  OBS: é importante verificar se o número fornecido pelo usuário corresponde ao número de elementos da lista, se não vai ocorrer um erro.

# Eu usei a mesma forma do exercício passado para acessar os elementos da lista anterior.

'''

