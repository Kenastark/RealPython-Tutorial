#%%
import pandas as pd

def read():
    return pd.read_csv("data-sets/olympics.csv", header=1).rename(columns={
        "Unnamed: 0": "country",
        "? Winter": "winter_olympics",
    })

olympics = read()
# %%
