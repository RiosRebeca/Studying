print("TESTANDO FUNÇÕES")



def diz_oi():
    print("OI!")
    return "Ola"

def diz_oi2():
    a = []
    return a

def diz_oi3():
    return "Ola"
    print("OI!")


diz_oi()
print(type(diz_oi2()))
a = diz_oi3()
print(a)


# Crie uma função que receba um número inteiro e devolve o seu dobro

def dobro(a:int):
   resultado = a * 2
   return resultado

resultado = dobro(3)
print(resultado)
