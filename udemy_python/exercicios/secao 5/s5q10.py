print("EXERCÍCIO 5 Q10")


s = int(input("Qual seu sexo biológico?\n    a) Homem\n    b) Mulher\n    "))

a = 0
b = 0

if s == a:
    print( a + 1)
elif s == b:
    print(b + 2)
else:
    print("dado inválido")

h = float(input("Qual sua altura?"))

p1 = (72 * h) - float(58)
p2 = (62.1 * h) - float(44.7)

if s == 1:
    print(p1)
elif s == 2:
    print(p2)
else:
    print("Resposta inválida")
