'''
crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos três lados de um triângulo. Elabore funções para:

A) Determinar se os lados formam um triângulo, sabendo que:
    O comprimenro de cada lado de um triângulo é menor do que a soma dos outros dois lados.

B) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo. Sendo que:
--> Chama-se equilátero o triângulo que têm três lados iguais.
--> Denominam-se isócseles o triângulo que tem o comprimenro de dois lados iguais.
--> Recebe o nome de escaleno o triângulo que tem os tres lados diferentes.
'''
  

def class_triangulo(a: int, b: int, c: int):
    if a + b > c or a + c < b or b + c < a:
        print("É um triângulo")
        if a == b and a == c and b == c:
            return "Triângulo equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    return "Não é um triângulo"


print(class_triangulo(2, 3, 4))
print(class_triangulo(2, 2, 2))
print(class_triangulo(4, 4, 2))
print(class_triangulo(3, 4, 9))