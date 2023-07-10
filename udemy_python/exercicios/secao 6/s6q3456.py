print("EXERCÍCIO - SEÇÃO 6")

# s6q3 

regressiva = 11 

while regressiva != 0:
    print(regressiva-1)
    regressiva -= 1    
    if regressiva == 1:
        print("FIM!")

# s6q4

for p in range(0,100001,1000):
    print(p)

# 3 s6q5

soma_total = 0

for _ in range(10):
    valor = int(input("Insira um valor: "))
    soma_total += valor

print("A soma dos valores é:", soma_total)

#s6q6

soma = 0 

for num in range(10):
    soma += num
    print((soma)/10)
