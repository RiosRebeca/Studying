import pandas as pd
import numpy as np

df = pd.read_csv("Cuisine_rating.csv")

print(df.head(2))
#print(df.describe())
#print(df.info())

location = df.groupby("Location")["Food Rating"].mean()
print(location)

