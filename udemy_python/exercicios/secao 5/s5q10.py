print("EXERCÍCIO 5 Q10")

'''
faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura)

homens: (72.7 * h) - 58
mulheres:(62.1 * h) - 44.7
'''

altura = float(input("Qual é a sua altura em metros? "))
sexo = input("Qual é o seu sexo (M para masculino, F para feminino)? ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é:", peso_ideal)
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é:", peso_ideal)
else:
    print("Sexo inválido. Por favor, insira M para masculino ou F para feminino.")

