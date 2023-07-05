print("MÓDULO 4")


"""
2 + 2 --> soma
2 - 2 --> subtração 
2 * 2 --> multiplicação
2 / 2 --> divisão que retorna um float
2 // 3 --> divisão que retorna um int
2 ** 2 --> elevado 
2 % 2 --> vai mostrar a sobra dessa divisão

se o num for par, a sobra da divisão será = 0, se for impar a sobra será = 1.
"""

idade = int(input("Qual a sua idade?"))
ano = 2023 - idade
print(f'você nasceu em {ano}')

'''
Quando usamos o "or" (ou), caso uma das afirmativas sejam verdadeiras ele irá considerar tudo como verdade. Ex.:

True or True --> True    False or True --> True
True or False --> True   False or False --> False

Das 4 possibilidades possíveis, 3 são consideradas verdadeiras. Vejamos o exemplo abaixo:
'''

frutas = int(input("Quantas frutas você tem?"))
if frutas > 10 or  frutas <= 50:
    print(True)
else:
    print(False)

'''
Quando usamos o "and" (e) ambas as alternativas devem ser verdadeiras para considerar como True. EX.:

True and True --> True    False and True --> False
True and False --> False  False and False --> False

Das 4 possibilidades possíveis, 3 são consideradas falsas. Vejamos como o mesmo exemplo:
'''

frutas = int(input("Quantas frutas você tem?"))
if frutas > 10 and  frutas <= 50:
    print(True)
else:
    print(False)

'''
Quando frutas = 100, o ex.1 printa "True" porque 100 é maior que 10, então a primeira condição é verdadeira, embora a segunda seja falsa já que 100 não é igual e nem menor que 50. Já no ex.2, o print sai "False" porque 100 é maior que 10, mas não é igual e nem menor que 50. Como as duas condições não foram atendidas, então ele printa "False".
'''
nome = "Pamella Negromonte"
print(nome)
print(nome.split())         # Transforma em uma lista de str ['Pamella', 'Negromonte']
print(len(nome))            
print(nome[0:7])            # output: ele vai escrever o nome "Pamella" (start, stop, step)
print(nome[8:18])           # output: "Negromonte" porque start no 8, stop 18 (um antes).
print(nome.upper())         # output: PAMELLA NEGROMONTE
print(nome.lower())         # output: pamella negromonte


