print("EXERCÍCIO 5 Q5")

'''
n = float(input("Insira um número: "))
if (n/float(2) == 0:
    print("Par")
elif (n/float(2) == 1:
    print("Ímpar")

ERRADO
'''

n = int(input("Insira um número: "))
if n % 2 == 0:
    print("Par")
else:
    print("Ímpar")


dividendo = int(input("Insira um núemro: "))
divisor = int(input("Insira um número: "))

resto = dividendo % divisor
print(resto)

'''
Nesse exemplo, o operador % é usado para calcular o resto da divisão entre dividendo e divisor. O valor de resto será igual a divisão do dividendo pelo divisor.
''' 