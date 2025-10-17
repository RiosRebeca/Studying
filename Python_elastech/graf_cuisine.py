import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


"""
Marital Status     object
Activity           object
Budget              int64
Cuisines           object
Alcohol            object
Smoker             object
Food Rating         int64
Service Rating      int64
Overall Rating    float64
Often A S          object
dtype: object
"""

df = pd.read_csv("Cuisine_rating.csv")

#sns.histplot(data=df, x="Cuisines", hue="Cuisines")
#plt.show()

#sns.countplot(data=df, x="Cuisines", hue="Location")
#plt.show()



