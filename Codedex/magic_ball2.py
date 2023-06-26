print("magic ball 2")

import random

duvida = input("Qual a sua dúvida?")
preparado = input("Você tem certeza que está preparado(a) para resposta da bola mágica?")

if preparado == "sim" or preparado == "s" or preparado == "S":
  resposta = random.randint(1,9)

  if resposta == 1:
    print("Sim, definitivamente!")
  elif resposta == 2:
    print("É decididamente assim.")
  elif resposta == 3:
    print("Sem dúvidas!")
  elif resposta == 4:
    print("Resposta nebulosa, tente de novo.")
  elif resposta == 5:
    print("Pergunte de novo mais tarde.")
  elif resposta == 6:
    print("Melhor não dizer agora.")
  elif resposta == 7:
    print("Minhas fontes dizem que não.")
  elif resposta == 8:
    print("Perpectivas não tão boas...")
  else:
    print("Duvido muito.")

else:
  print("Então volte mais tarde.")