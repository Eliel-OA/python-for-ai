import pandas as pd

df = pd.read_csv("pokemons.csv")


df = df.drop_duplicates()
df