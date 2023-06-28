#!C:\Users\eurek\AppData\Local\Microsoft\WindowsApps\python3

print("df1.2")


lista = ["agua", 2, 3.4, ["terra"], casa, 6, 1235.56, "ar", casa, 777, 666, 999, 3.14, "Fogo", "Shemhamphorasch"]

s = 0
f = 0
i = 0

for obj in lista:
  if type(obj) ==  str:
      s = s + 1
  elif type(obj) == int:
      int = int + 1
  elif type(obj) == float:
      f = f + 1

prit("str")
print("float")
print("int")

