print("currency")

peso=input("quantos soles você tem?")
reais=input("quantos resias você tem?")
soles=input("quantos soles você tem?")

dolar = (float(peso)*0.004) + (float(soles)*0.28) + (float(reais)*0.21)

print("No total você tem"+ str(dolar))

#o 'dolar' retorna em float por isso transforma ele em str



