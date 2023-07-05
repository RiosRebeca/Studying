#!C:\Users\eurek\AppData\Local\Microsoft\WindowsApps\python3

print("PROGRAMAÇÃO EM FÍSICA 1")

start = input("Vamos aplicar os conhecimentos de python em física mecânica?")
if start == 'sim' or start == 's' or start == 'S':
    print("Vamos começar.")
else:
    print("Vamos começar mesmo assim.")

"""
2 + 2 --> soma
2 - 2 --> subtração 
2 * 2 --> multiplicação
2 / 2 --> divisão que retorna um float
2 // 3 --> divisão que retorna um int
2 ** 2 --> elevado 
2 % 2 --> vai mostrar a sobra dessa divisão

se o num for par, a sobra da divisão será = 0, se for impar a sobra será = 1.
"""
print("FUNÇÃO HORÁRIA DE DESLOCAMENTO")

q1 = input("Um móvel com velocidade constante igual a 20 m/s parte da posição 5 m de uma reta numerada e anda de acordo com o sentido positivo da reta. Determine a posição do móvel após 15 s de movimento.\n    a) 105 m\n    b) 205 m\n    c) 305 m\n    d) 405 m\n    e) 505 m\n")

a = 105
b = 205
c = 305
d = 405
e = 505

if q1 == 305 or q1 == c:
    print("Parabéns!")
else:
    print("Tente novamente.")

print("Vamos conferir a resposta.\n    OBS: lembre-se de utilizar as unidades de medida corretamente.")

s0 = int(input("insira a posição inicial:"))
v = int(input("insira a velocidade:"))
ti = int(input("insira o tempo inicial:"))
tf = int(input("insira o tempo final:"))
dt = (tf - ti)

s = s0 + (v * dt)
print(f'A resposta é {s}')



