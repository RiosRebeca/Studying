'''
Faça uma função que receba por parâmetro dois valorez x e z. Calcule e retorne o resultado de x**z para o programa principal. ATENÇÃO: não utilize nenhuma função pronta de exponenciação.
'''

def expo(x: int, z:int):
    return x ** z

x = int(input("Insira o valor de X: "))
z = int(input("Insira o valor de Z: "))

res = expo(x, z)

print(f"O resultado é {res}")


# OU

def expo_2():
   x_2 = int(input("INSIRA O VALOR DE X: "))
   z_2 = int(input("INSIRA O VALOR DE Z: "))
   return x_2 ** z_2

res_2 = expo_2()

print(res_2)