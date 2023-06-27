print("Advinhe")

tentativas = 0
guess = 0

while guess != 6:
  guess = int(input("adivinhe o número:"))
  tentativas = tentativas + 1 
  print("Tentativas restantes: " + str(7 - tentativas))
  if tentativas >= 7:
    print("Acabou as tentativas")
    exit()

print("Você conseguiu!")
