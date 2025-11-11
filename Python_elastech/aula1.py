# Dados aula 1

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("playlists_tracks.csv")
#print(df.head())
#print(df.info()) # ideal para ver o nome das colunas e var nulos
#print(df.columns)
#print(df.shape)

# LIMPEZA E EXTRAÇÃO DE DADOS

df["album_release_date_ajustado"] = pd.to_datetime(df["album_release_date"], errors="coerce")
#print(df.columns)

df["album_release_date"] = df["album_release_date_ajustado"].dt.year
#print(df.head(2))

pl_track_clean = df.dropna(subset="track_name")
#print(pl_track_clean.shape)




# VIZUALIZAÇÃO COM MATPLOTLIB

# Qual playlist tem mais músicas?

#print(df["playlist_name"].value_counts().max()) #output: 311
 
max_pl = (pl_track_clean["playlist_name"].value_counts().idxmax())
min_pl = (pl_track_clean["playlist_name"].value_counts().idxmin())
#print(f"A playlist com maior quantidade de músicas é: {max_pl}")
#print(f"A playlist com menor quantidade de músicas é: {min_pl}")

pl_counts = pl_track_clean["playlist_name"].value_counts().head(10)
#print(pl_counts)

pl_counts.plot(kind="barh", figsize=(8,5))
plt.title("TOP 10 playlists com mais músicas")
plt.xlabel("Quantidade de músicas")
plt.ylabel("")
#plt.show()

plt.style.use("seaborn-v0_8")

# Como evolui a quantidade de músicas lançadas por ano?

musica_ano = pl_track_clean["album_release_date"].value_counts().sort_index()
#musica_ano.plot(kind="line", marker="o", figsize=(8,4))
#plt.show()



# Quais são os arrtistas com maior popularidade média?

artista_pop = pl_track_clean.groupby("artist_names")["popularity"].mean().sort_values(ascending=False).head(10)
#print(artista_pop)
#artista_pop.plot(kind="", x="artist_names", figsize=(8,5))
#plt.show()


# Quais os artistas mais frequêntes nas playlists?

#print(pl_track_clean.columns)

freq_artista = pl_track_clean.groupby("album_name")["artist_names"].value_counts().sort_values(ascending=False).head(5)
#print(freq_artista)
#freq_artista.plot(kind="line")
#plt.show()



# Quais gêneros são mais frequentes nas playlists?

genero_artistas = pd.read_csv("genres_artists.csv")
#print(genero_artistas.head(4))
#print(genero_artistas.columns)

# EXPLODIR OS GÊNEROS (1 linha por artista e gênero)

genero_artistas["lista_generos"] = genero_artistas["genres"].fillna("").str.split(",")
#print(genero_artistas.head(3))

genero_artistas_explodidos = genero_artistas.explode("lista_generos")
#print(genero_artistas_explodidos.head(3))

genero_artistas_explodidos.drop(columns=["genres", "Unnamed: 0"], inplace=True)
#print(genero_artistas_explodidos.head(3))

genero_explodido_limpo = genero_artistas_explodidos[genero_artistas_explodidos["lista_generos"] != ""]
genero_explodido_limpo["lista_generos"].unique()
#print(genero_explodido_limpo.head(3))


# 








