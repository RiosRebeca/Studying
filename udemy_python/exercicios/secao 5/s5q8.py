print("EXERCÍCIO 5 Q8")

a1 = int(input("Informe a nota da A1: "))
a2 = int(input("Informe a nota da A2: "))

nota = (a1 + a2)/2

if a1 >= 0 and a1 <= 10 and a2 >= 0 and a2 <= 10:
    print(nota)
else:
    print("Número (s) invalido (s)")