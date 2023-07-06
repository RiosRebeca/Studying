print("MÓDULO 5")

# Condicionais if, elif e elif

catalogo = 5300
livre = 2500
l14 = 1100
l16 = 1000

idade = int(input("Qual sua idade?"))
if idade < 18 and idade < 14:
   print(f'você tem {livre} filmes para assistir')
elif idade >= 14 and idade < 16:
   print('você tem' + str( livre + l14))
elif idade >= 16 and idade > 18:
   print('você tem' + str ( livre + l14 + l16))
else:
   print('você tem' + str ( catalogo))

'''
Operadores binários:

Para o "and", ambos os valores precisam ser True.
Para o "or", um ou outro valor precisa ser True.
Para o "is", o valor é comparado com um segundo valor.

Operadores unários:

Para "not", o valor do booleano é invertido, se for True vira False, se for False vira True.
'''


