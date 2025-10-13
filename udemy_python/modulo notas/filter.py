# FILTER

'''
A função embutida filter() é como o map(), ela vai receber dois parâmetros, o primeiro vai ser uma função e a segunda o que ela vai iterar.

--> SINTAXE

filter(função, iteravel)

O filter() vai retornar True and False. Assim como o map(), ele desaparece depois de ser executado.
'''

# FORMA MANUAL

numeros = 1, 2, 3, 4, 5, 6  # Criando uma tupla

media_teste = sum(numeros)/len(numeros)  # sum() vai iterar e somar os elementos
                                   # len() vai retornar o número do tamanho (6)
print(media_teste)

# FORMA MAIS SUCINTA

import statistics 

media = statistics.mean(numeros)  # Aqui ele já cria a média

res = list(filter(lambda x: x > media, numeros)) # Pega elementos ACIMA da média
print(res)


nomes = ['Claudia Alves', 'Pamella', 'Joel', 'Fagner', 'Mateus', 'Rebeca', '', '', '', '', '', '']

res_nomes = list(filter(None, nomes))  # Ele vai tirar o que está fazio
print(res_nomes)                       # também da pra fazer com len()


last = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) > 7, nomes)))

print(last)