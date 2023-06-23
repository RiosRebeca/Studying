print("grades")

t1=int(input("valor do teste 1"))
t2=int(input("valor do teste 2"))
t3=int(input("valor do teste 3"))
t4=int(input("valor do teste 4"))

grade = (t1 + t2 + t3 + t4)/4
print(grade)

if grade > 70:
 print("Você passou!")
else:
 print("Nos vemos no próximo semestre")