print("EXERCÍCIO - SEÇÃO 6")

'''
Escreva um algoritimo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algorítimos que compõe o número.


--> "leia" então é um input e tem que ser int
--> eu vou ter que "percorrer" esse input
--> "imprimir" é um print e eu vou ter que fazer isso para cada numero que compõe o int
--> como vou separar cada elemento de um inteiro?
'''

numero = input("Digite um número: ")  # Vai retornar em str

for digito in numero:                 # Vai armazenar o numero no digito
   list(str(digito))
   print(digito) 

# Output: repete o valor do último algorítimo do numero int...n é isso que eu quero


'''
numero = input("Digite um número: ")  

for digito in numero:                 
   list(str(numero))
   print(numero) 
'''