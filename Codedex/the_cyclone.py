print("The cyclone")

altura=int(input("qual altura?"))
creditos=int(input("quantos créditos?"))

if altura >= 137 and  creditos >=10:
  print("Aproveite o passeio!")

elif altura < 137:
  print("Você não é alto o suficiente para o passeio.")

elif creditos < 10:
  print("Você não tem créditos suficientes.")

else:
  print("Dados invalidos.")

