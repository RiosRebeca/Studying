#!C:\Users\eurek\AppData\Local\Microsoft\WindowsApps\python3

print("df1.2")

casa = 99 + 105
lista = ["agua", 2, 3.4, ["terra"], casa, 6, 1235.56, "ar", casa, 777, 666, 999, 3.14, "Fogo", "Shemhamphorasch"]

s = 0
f = 0
i = 0

for obj in lista:
  if type(obj) ==  str:
      s = s + 1
  elif type(obj) == int:
      i = i + 1
  elif type(obj) == float:
      f = f + 1

print(s, "número de str dentro da lista")
print(f, "número de float dentro da lista")
print(i, "número de int dentro da lista")
