'''
Faça uma função que receba que receba em Km e a quantidade de litros de uma gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

1 - menor que 8 : venda o carro! 
2 - 8 e 12 econômico!
3 - maior que 12 Super econômico!
'''

def consumo(km: int, l: int):
    res = km//l
    if res < 8:
        return "Venda o carro!"
    elif res == 8 and res <= 12:
        return "Econômico!"
    elif res >= 12:
        return "Super econômico!"
 

print(consumo(123, 4))