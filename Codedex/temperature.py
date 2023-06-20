print("temperature")

print(1+1) #operações de inteiros
a=2
b=7
print(a+b)    
print(a-b)
print(a*b)
print(a/b)

x=37
y=49
resposta= x+y

conta=input("Qual o valor de 37+49?")   #O input SEMPRE RETORNA EM STRING
print("sua resposta foi"+conta)
print("A resposta correta é"+ str(resposta))


acertou = resposta == int(conta)
print("Voce acertou ? \n" + str(acertou))

#---------------------------------------------

fahrenheit=input("qual a tenperatura em Fahrenheit?")
celsius=(float(fahrenheit)-float(32))/1.8

print("A temperatura em Celsius é"+str(celsius))


