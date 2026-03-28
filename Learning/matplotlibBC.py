import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


print(f"Current cwd: { os.getcwd()}",)

df = pd.read_csv("../Learning/pokemons.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.plot(type_count.index, type_count.values, color="red", )

plt.title("Number of pokemon by primary Type")

plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()

plt.show()
