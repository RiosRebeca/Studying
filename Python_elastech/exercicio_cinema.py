import pandas as pd
import numpy as np 

df = pd.read_csv("cinemas.csv")
print(df.head(2))


filme_menor = df[df['bilheteria'] == df['bilheteria'].min()]['filme']
filme_maior = df[df['bilheteria'] == df['bilheteria'].max()]['filme']

#print(f"O FILME COM MENOR BILHETERIA FOI: {filme_menor}")
#print(f"O FILME COM MAIOR BILHETERIA FOI: {filme_maior}")

grupo1 = df.groupby("cidade")["bilheteria"].count()
print(grupo1)


#grupo2a = df.groupby(["cidade", "filme"])["bilheteria"].count()
#print(grupo2a)
grupo2b = df.groupby(["cidade", "filme"])["bilheteria"].sum()
print(grupo2b)

grupo2c = df.groupby(["cidade", "filme"]).agg({"bilheteria":["mean", "max", "min"]})
print(grupo2c)