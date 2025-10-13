#i#mport os 
import pandas as pd
import numpy as np 

#print(os.chdir("archive"))
#print(os.listdir())

df = pd.read_csv("clientes.csv")
print(df.columns)

#print(df.head(2))
#print(df.tail(9))

#print(df.info)
#print(df.dtypes)


# A lógica é: do grupo x pegue y e faça z
resp = df.groupby("cidade")["valor_mensal"].mean()
print(resp)