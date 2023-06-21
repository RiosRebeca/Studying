print("BMI")

mass=input("Qual seu peso?")             #a resposta vai retornar em str
height=input("qual sua altura")          #a resposta vai retornar em str

#tanto mass como height são str e não realizam op mat

bmi = float(mass)/float(int(height)**2)
#bmi=int(mass)/int(height)**2
print(bmi)

print(type(bmi))                         
#print("eu IMC é" + float(bmi))

#y = funcao(x), o que vem antes do = só armazena
#copo = maquinaDeExtrairSuco(fruta)

#o 'height1 é uma str e deve ser transformado em int p/ ** c/ '2' q é um int
#depois o int será convertido em float para realizar a operação float c/float
#no primeiro ex. eu só poderia medir a altura em cm '157', no segundo, c/ float
#eu posso medir em m "1m57cm"= 1.57
--------------------------------------------------------------------------------

