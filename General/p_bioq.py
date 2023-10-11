print("PERFIL BIOQUÍMICO")

paciente = {}

numero = int(input("Digite o número do paciente: "))
nome = input("Digite o nome completo do paciente: ")
sexo = input("Digite o sexo do paciente: ")
idade = int(input("Digite a idade do paciente: "))

paciente['Número'] = numero
paciente['Nome'] = nome.upper()
paciente ['Sexo'] = sexo.upper()
paciente['Idade'] = idade

print("Informações do Paciente")

for chave, valor in paciente.items():  # A função items() retorna c/v
    print(f'{chave}: {valor}')    

exames_paciente = {}


print("Avaliação da Glicemia")

at = float(input("Insira o valor da ABSORBÂNCIA DO TESTE: "))
ap = float(input("Insira o valor da ABSORBÂNCIA DO PADRÃO: "))

glicose = (int(at)/int(ap))*100
fator_calibração = 100/int(ap)

if glicose > 500:
    print("Reconmenda-se que a amostra seja diluída e o valor seja medido novamente.")
    v_diluir = int(input("Insira a quantidade de vezes que a amostra doi diluída: "))
    glicose_c = glicose * v_diluir
elif glicose <= 70:
    print(f'O valor da glicose em jejum é: {glicose}(mg/dL), e está abaixo do valor reconmendado.')
elif glicose == 70 and glicose <= 99:
    print("O valor da glicose de jejum é: {glicose}(mg/dL)")
elif glicose == 100 and glicose <= 125:
    print(f'O valor da glicose de jejum é: {glicose}(mg/dL), e está alterada')
else:
    print(f'O valor da glicose em jejum é: {glicose}(mg/dL), e indica uma provável diabetes.')
    
exames_pacientes["Glicose"] = glicose

print("Avaliação do Ferro")     

a1=float(input("Insira o valor de absorbância 1: "))
a2=float(input("Insira o valor da absorbância 2: "))
ap=float(input("Insira o valor da absorbância padrão: "))

ferro = ((int(a2) - int(a1)) / int(ap)) * 500  # (µ/mL)
if ferro >= 50 and ferro <= 150:
    print(f"O valor do ferro é  {ferro}(µg/mL) e está dentro do recomendado")
elif ferro < 50:
    print(f"O valor do ferro é {ferro}(µg/mL) e está abaixo do recomendado")
else:
    print(f"O valor do ferro é {ferro}(µg/mL) e está acima do valor reconmendado")

fc = 500/int(ap)

ferro_serico = (int(a2)-int(a1)) * fc

if ferro_serico < 50 or ferro_serico > 150:
    print(f"O valor do ferro sérico é {ferro_serico}(µg/mL) e está dentro do recomendado")
elif ferro_serico < 50:
    print(f"O valor do ferro sérico é {ferro_serico}(µg/mL) e está abaixo do valor recomendado")
else:
    print(f"O valor do ferro sérico é {ferro_serico}(µg/mL) e está acima do recomendado")

# Capacidade de ligação de ferro

cllf = 500 - (ferro)      # Capacidade latente de ligação ao ferro

if cllf >= 140 and cllf <= 280:
    print(f"Sua CLLF é {cllf}(µg/dL) e está dentro do valor reconmendado")
elif cllf < 140:
    print(f"Sua CLLF é {cllf}(µg/dL) e está abaixo do valor reconmendado")
else:
    print(f"Sua CLLF é {cllf}(µg/dL) e está acima do valor reconmendado")

ctlf = ferro_serico + cllf   # capacidade total de ligação ao ferro

if ctlf >= 250 and ctlf <= 400:
    print(f'O valor da CTLF é de {ctlf}(µg/dL) e está dentro do valor recomendado.')
elif ctlf < 250:
     print(f'O valor da CTLF é de {ctlf}(µg/dL) e está abaixo do valor recomendado.')
else:
      print(f'O valor da CTLF é de {ctlf}(µg/dL) e está acima do valor recomendado.')


ist = (ferro_serico//ctlf) * 100  # indice de saturação transferrina

if ist >= 20 and its <= 50:
     print(f'O valor do IST é de {ist}(%) e está dentro do valor recomendado.')
elif ist < 20:
     print(f'O valor do IST é de {ist}(%) e está abaixo do valor recomendado.')
else:
      print(f'O valor do IST é de {ist}(%) e está acima do valor recomendado.')



exames_pacientes['Ferro'] = ferro
exames_pacientes['Ferro sérico'] = ferro_serico
exames_pacientes['CLLF'] = cllf
exames_pacientes['CTLF'] = ctlf
exames_pacientes['IST %'] = ist




