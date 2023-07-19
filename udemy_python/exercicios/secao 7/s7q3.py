print("EXERCÍCIOS - SEÇÃO 7")

# s7q3

'''
Ler um conjunto de números reais, armazene-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
'''

import math                                    # Importa a classe para poder usar

numeros = [14, 6, 13, -9, 65, -237, 0, -15]    # Armazena valores na lista
resultados = []                                # Cria uma lista em branco para colocar os valores

for valores in numeros:                        # Armazena os elementos contidos em numeros em valores
    raiz_quadrada = math.sqrt(abs(valores))    # abs() tem que transformar pra absoluto se n não corre
    resultados.append(raiz_quadrada)           # Aqui ele vai add os valores obtidos na ação anterior

print(resultados)                              # Vai mostrar os resultados armazenados em 'resultados'



