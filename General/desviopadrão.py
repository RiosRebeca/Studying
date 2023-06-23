print("desvio padrão")

x1=int(input("qual o valor mínimo?"))
x2=int(input("qual o valor máximo?"))

m = (x1+x2)/2  #retorna inteiro

psoma=(x1 - m)**2
ssoma=(x2 - m)**2
divisao = (psoma+ssoma)/2

DV = float(divisao)**0.5

print(m,psoma,ssoma,divisao,DV)

