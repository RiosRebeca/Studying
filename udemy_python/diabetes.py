print("FLUXOGRAMA - DIAGNÓSTICO DE DIABETES")

nome = input(f"INSIRA O NOME COMPLETO DO PACIENTE: ")
data = input(f"INSIRA A DATA DE NASCIMENTO: ")
numero = input("INSIRA O NÚMERO DO PACIENTE: ")

paciente = {"Paciente":nome , "Data de Nascimento": data, "Número":numero}

print(paciente) 

check = input("CONFIRME AS INFORMAÇÕES DO PACIENTE\n a) Digite SIM caso as informações estejam corretas;\n b) Digite NÃO caso alguma informação não esteja correta.\n  ")
while check == "NÃO":
    nome = input(f"INSIRA O NOME COMPLETO DO PACIENTE: ")
    data = input(f"INSIRA A DATA DE NASCIMENTO: ")
    numero = input("INSIRA O NÚMERO DO PACIENTE: ")
    check = input("CONFIRME AS INFORMAÇÕES DO PACIENTE\n a) Digite SIM caso as informações estejam corretas;\n b) Digite NÃO caso alguma informação não esteja correta.\n  ")
     
print("Prossiga preenchendo as perguntas com letras maiúsculas.") 

info_paciente = {}
# info_paciente["Chave"] = Valor

jejum = input("O PACIENTE ENCONTRA-SE EM JEJUM?\n 1) SIM\n 2) NÃO\n ")

if jejum == "NÃO":
    print("Para aferir a glicose, é necessário que o paciente esteja em jejum de 8-12h.")
else:
    hora = input("Informe a hora da última refeição:\n  ")

info_paciente["Sexo"] = 0
info_paciente["gestante"] = 0 
info_paciente["Glicose da gestante"] = 0
info_paciente["Teste de Tolerância a Glicose"] = 0
info_paciente["Glicose"] = 0
info_paciente["Glicose 2"] = 0
info_paciente["OGTT 0 min"] = 0
info_paciente["OGTT 120 min"] = 0

resultado = []

sexo = input("Informe o sexo do paciente:\n a) FEMININO\n b) MASCULINO:\n  ")

if sexo == "FEMININO":
    gestante = input("A paciente encontra-se em proceso de gestação?\n ")
    if gestante == "SIM":
        print("Recomenda-se fazer o rastreio gestacional.")
        glicoseg = int(input("INSIRA O VALOR DA GLICOSE: "))
        resultado.append(glicoseg)
        if glicoseg < 85:
            print("Caso a paciente não possua 2 ou mais fatores de risco: RASTREIO NEGATIVO")
            print("Caso a paciente possua 2 ou mais fatores de riscos: REPETIR A GLICEMIA EM JEJUM A PARTIR DA SEMANA 20.")
        elif glicoseg >= 85 and glicoseg <= 109:
            print("RESULTADO: RASTREIO POSITIVO")
            print("Recomenda-se fazer o Teste de Tolerância a Glicose entre 24 e 28 semanas.")
            ttg = int(input("INSIRA O VALOR DO TTG: "))
            resultado.append(ttg)
            if tgg >= 110:
                print(" RESULTADO: Diabetes gestacional.")
            else:
                print("RESULTADO: Recomenda-se repetir o teste. Caso os valores estejam igual ou acima de 110 mg/dL, DIANETES GESTACIONAL.")             
    else:
        print("PACIENTE NÃO É GESTANTE")
        gestante = "NÃO"
else:
    print("Caso não haja nenhuma especificação, siga preenchendo os campos.")
    gestante = "NÃO"

glicose = int(input("INSIRA O VALOR DA GLICOSE: "))
resultado.append(glicose)

if glicose <= 99:
    print(f"Glicose: {glicose} mg/dL")
    print("RESULTADO: glicose dentro dos níveis de referência")
   
elif glicose >= 100 and glicose <= 125:
    print(f"Glicose: {glicose} mg/dL")
    print("RECOMENDA-SE FAZER O TESTE DE SOBRECARGA A GLICOSE VIA ORAL.")
    ogtt0 = int(input("INSIRA O VALOR DO TESTE DE SOBRECARGA A GLICOSE VIA ORAL NO TEMPO 0 min: "))
    ogtt120 = int(input("INSIRA O VALOR DO TESTE DE SOBRECARGA A GLICOSE VIA ORAL NO TEMPO 120 min: "))
    if ogtt0 >= 100 and ogtt0 <= 125 and ogtt120 < 140:
        print("RESULTADO: Intolerância a glicose em jejum.")
    elif ogtt0 >= 100 and ogtt0 <= 125 and ogtt120 >=140 and ogtt120 <= 199:
        print("RESULTADO: Intolerância a glicose.")
    elif ogTt0 >= 100 and ogtt0 <= 125 and ogtt120 >= 200:
        print("RESULTADO: Diabetes Mellitus.")
        
else:
      print(f"Glicose: {glicose} mg/dL")
      print("RECOMENDQA-SE FAZER UM SEGUNDO TESTE.")
      glicose2 = int(input("INSIRA O VALOR DA GLICOSE NO TESTE 2: "))
      if glicose2 >= 126:
           print(f"Glicose: {glicose2} mg/dL")
           print("RESULTADO: Diabetes mellitus")
       
      else:
           print(f"Glicose: {glicose2} mg/dL")
           print("RESULTADO: não diabético")
            

print(paciente)
print(info_paciente)
print(resultado)

    