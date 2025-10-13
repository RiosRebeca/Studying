print("INFORMAÇÕES IMPORTANTES")

from sys import getsizeof   # retorna a qauntidade de bytes em memória do 
                            # elemento passado como parâmetro
print(getsizeof('Geek'))    # mostra quanto espaço a str está ocupando 


list_com = getsizeof([x for x in range(1000)])


# OBS: sets não tem valores repetidos!!!
# OBS2: sets não guardam ordens


# FORMANDO DICT COMPREHENSIONS

numeros = [1, 2, 3, 4, 5, 6]
dict = {numeros: valor ** 2 for valor in numeros}

# SINTAXE DE SORTED()

sorted(iterable, key=None, reverse=False)




