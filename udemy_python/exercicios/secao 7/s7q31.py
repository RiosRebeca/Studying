print("EXERCÍCIO - SEÇÃO 7")

# s7q31

'''
Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:

--> soma entre x e y : soma de cada elemento de x com cada elemento da mesma posição de y

--> Protudo entre x e y: multiplicação de cada elemento (..)

--> Diferença entre x e y

--> Interseção entre x e y: apenas os elementos que aparecem nos dois vetores.

--> União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.

'''

v1 = []
v2 = []

for i in range(5):
    n = int(input("INSIRA UM NÚMERO NA LISTA 1: "))
    v1.append(n)

for j in range(5):
    m = int(input("INSIRA UM NÚMERO NA LISTA 2: "))
    v2.append(m)

print(f'Esses são os componentes da lista 1: {v1}')                                                      
print(f'Esses são os componentes da lista 2: {v2}')

v_soma = []
v_multiplicacao = []
v_diferenca = []

for a in range(len(v1)):                       # Lógica: para percorrer e acessar o indice, lembre que é só acessar o número que está percorreno no momento
    soma = v1[a] + v2[a]
    v_soma.append(soma)
    multiplicacao = v1[a] * v2[a]
    v_multiplicacao.append(multiplicacao)
    diferenca = v1[a] - v2[a]
    v_diferenca.append(diferenca)

print(f'Essa é a soma entre x e y: {v_soma}')
print(f'Essa é a multiplicação entre x e y: {v_multiplicacao}')
print(f'Essa é a diferença entre x e y: {v_diferenca}')

conj_v1 = set(v1)                                                   # P/ tranformar em set tem que atribuir a uma variável
conj_v2 = set(v2)

inter = conj_v1.intersection(conj_v2)
uniao = conj_v1.union(conj_v2)

print(f'Essa é a intersecção entre os dois grupos: {inter}')
print(f'Essa é a união entre os dois grupos: {uniao}')
