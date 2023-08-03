print("EXERCÍCIO - SEÇÃO 7")

# s7q24

'''
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros números naturais que são múltiplos de 7 ou que terminam com 7.
'''

m_lista = []

for lista in range(1,701):
    if lista % 7 == 0:
        m_lista.append(lista)


print(m_lista)       

print(f"A quantidade de componentes dentro da lista é: {len(m_lista)}.")