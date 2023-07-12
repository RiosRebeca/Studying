#!C:\Users\eurek\AppData\Local\Microsoft\WindowsApps\python3

print("Avaliação do ferro.upper()")     

a1=int(input("Insira o valor de absorbância 1: "))
a2=int(input("Insira o valor da absorbância 2: "))
ap=int(input("Insira o valor da absorbância padrão: "))

ferro = ((a2 - a1) / ap) * 500  # (µ/mL)
if ferro >= 50 and ferro <= 150:
    print(f"O valor do ferro é  {ferro}(µg/mL) e está dentro do recomendado")
elif ferro < 50:
    print(f"O valor do ferro é {ferro}(µg/mL) e está abaixo do recomendado")
else:
    print(f"O valor do ferro é {ferro}(µg/mL) e está acima do valor reconmendado")

fc = 500/ap

ferro_serico = (a2-a1) * fc
if ferro_serico < 50 or ferro_serico > 150:
    print(f"O valor do ferro sérico é {ferro_serico}(µg/mL) e está dentro do recomendado")
elif ferro_serico < 50:
    print(f"O valor do ferro sérico é {ferro_serico}(µg/mL) e está abaixo do valor recomendado")
else:
    print(f"O valor do ferro sérico é {ferro_serico}(µg/mL) e está acima do recomendado")

#Capacidade de ligação de ferro

cllf = 500 - (ferro)
if cllf >= 140 and cllf <= 280:
    print(f"Sua CLLF é {cllf}(µg/dL) e está dentro do valor reconmendado")
elif cllf < 140:
    print(f"Sua CLLF é {cllf}(µg/dL) e está abaixo do valor reconmendado")
else:
    print(f"Sua CLLF é {cllf}(µg/dL) e está acima do valor reconmendado")


#Capacidade total de ligação de ferro

ctlf = ferro_serico + cllf
if ctlf >= 250 and cllf <= 400:
    print(f"Sua CLLF é {ctlf}(µg/dL) e está dentro do valor reconmendado")
elif ctlf < 250:
    print(f"Sua CLLF é {ctlf}(µg/dL) e está abaixo do valor reconmendado")
else:
    print(f"Sua CLLF é {ctlf}(µg/dL) e está acima do valor reconmendado")


#Índice de saturação da transferrina

its = (ferro_serico/ctlf) * 100    
if ctlf >= 20 and cllf <= 50:
    print(f"Sua CTLF é {its}% e está dentro do valor reconmendado")
elif ctlf < 20:
    print(f"Sua CTLF é {its}% e está abaixo do valor reconmendado")
else:
    print(f"Sua CTLF é {its}% e está acima do valor reconmendado")                



