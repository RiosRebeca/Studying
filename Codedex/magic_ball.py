print("magic ball")

import random

duvida = input("Qual sua dúvida?")
preparado = input("Você está preparado para resposta da bola mágica?")

resposta = random.choice(['a','b','c','d','e','f','g','h','i'])

if resposta == 'a':
  print("Sim, definitivamente")
elif resposta == 'b':
  print("É decididamente assim")
elif resposta == 'c':
  print("Sem dúvidas")
elif resposta == 'd':
  print("Resposta nebulosa, tente de novo")
elif resposta == 'e':
  print("Pergunte novamente mais tarde")
elif resposta == 'f':
  print("Melhor não te dizer agora")
elif resposta == 'g':
  print("minhas fontes dizem que não")
elif resposta == 'h':
  print("Perspectivas não tão boas")
else:
  print("Muito duvidoso")
#-------------------------------------------------------------------------------------------
# Algumas observações: random.radint != random.choice, o primeiro vai selecionar números int
# enquanto o segundo vai selecionar elementos de uma lista. Para fazer uma lista é necessário
# usar []