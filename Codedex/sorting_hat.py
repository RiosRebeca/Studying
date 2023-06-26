print("Sorting Hat")

# '=' define variável '==' define comparação

gryffinor = 0  
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1=int(input("Q1) Do u like dawn or dusk?\n    1) Dawn \n    2) Dusk "))
if q1==1:
  gryffinor = gryffinor + 1 
  ravenclaw = ravenclaw + 1
elif q1==2:
  hulfflepuff = hulfflepuff + 1
  slytherin = slytherin + 1
else:
   error

q2=int(input("when i'm dead, i wnat people remember me as:\n    1) the good\n    2)the great\n    3) the wise\n    4) the bold"))
if q2==1:
  hufflepuff = hufflepuff + 2
elif q2==2:
  slytherin = slytherin + 2
elif q2==3:
  ravenclaw = ravenclaw + 2
elif q2==4:
  gryffindor = gryffindor +2 
else:
  error

q3=int(input("whick kind of instrument most pleases ur ear?\n    1) the violin\n    2) the trumpet\n    3)the piano\n    4) the drum"))
if q3==1:
  slytherin = slytherin + 4
elif q3==2:
  hufflepuff = hufflepuff + 4
elif q3==3:
  ravenclaw = ravenclaw + 4
elif q3==4:
  gryffindor = gryffindor + 4
else:
 error

if gryffinor > hufflepuff and gryffinor > ravenclaw and gryffinor > slytherin:
  print("gryffinor")
elif slytherin > hufflepuff and slytherin > gryffinor and slytherin > ravenclaw:
  print("slytherin")
elif hufflepuff > slytherin or hufflepuff > gryffinor or hufflepuff > ravenclaw:
  print("hufflepuff")
elif ravenclaw > slytherin or ravenclaw > gryffinor or ravenclaw > hufflepuff:
  print("ravenclaw")

