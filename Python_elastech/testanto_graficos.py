import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

"""
OBS: antes de importar as bibliotecas, certifique-se que instalou no ambiente correto.

/path/correto/pasta_com_arquivos Pipenv shell --> para usar o shell
Pipenv install {A biblioteca que você quer}
"""

df = pd.read_csv("clientes.csv")

#print(df.head(2))
#print(df.columns)
#print(df.dtypes) 

#media_cidade = df.groupby("cidade")["valor_mensal"].mean()
#print(media_cidade)


#sns.histplot(data=df, x="cidade", hue="cidade", kde=True).set_title("Distribuição por Cidade")
#plt.show()

#Testando a criação de vários gráficos
#for i in df.drop(columns=["gênero","nome"]):
#    sns.barplot(data=df, x=df["plano"], hue=df["cidade"], y=i, ci = 90)
#    plt.show() 

"""""
Qual a razão entre o valor da mensalidade e o numero de reclamacoes ? 
ha alguma relacao ? e por que ? tem alguma faixa etaria especifica ? alguma regiao ?
"""

sns.histplot(data= df, x="valor_mensal", y="reclamacoes")
plt.show()