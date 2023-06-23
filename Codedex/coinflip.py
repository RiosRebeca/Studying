print("coin flip")

import random

num = random.randint(0,1)

if num > 0.5:
  print("Heads")
else:
  print("Tails")
#-----------------------------------------

s0=int(input("Qual o valor de s0?"))
v=int(input("Qual o valor de v?"))
t2=int(input("Qual o valor de t2?"))
t1=int(input("Qual o falor de t1?"))

s = s0 + v*(t2-t1)

print(s)

if s > 100:
  print("você foi muito longe")

