print("Fizz Buzz")


for fb in range(0,101,1):
  print(fb)
  if fb % 3 == 0 and fb % 5 == 0:
     print("fizzbuzz")
  elif fb % 5 == 0:
     print("buzz")
  elif fb % 3 == 0:
     print("fizz")

#OBS: lembrar que o programa ler de cima para baixo, por isso é necessário pestar atenção na #ORDEM para que tenha lógica