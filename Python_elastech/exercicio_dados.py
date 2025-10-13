import pandas as pd
import numpy as np 

df = pd.read_csv("cinemas.csv")
#print(df.head(2))

print(df[df['bilheteria'] == df['bilheteria'].min()]['filme'])
print(df[df['bilheteria'] == df['bilheteria'].max()]['filme'])

