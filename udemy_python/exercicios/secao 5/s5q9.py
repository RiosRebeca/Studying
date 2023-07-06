print("EXERCÍCIO 5 Q9")

s = float(input("Insira o salário: "))
e = float(input("Valor do emprestimo: "))

p = (e/s) * float(100)

if p >= 20:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")

print(p)