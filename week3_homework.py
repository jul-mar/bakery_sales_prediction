import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_umsatz = pd.read_csv("umsatzdaten_gekuerzt.csv")
print(df_umsatz.head())

df_kiwo = pd.read_csv("kiwo.csv")
print(df_kiwo.head())

df_wetter = pd.read_csv("wetter.csv")
print(df_wetter.head())

df_umsatz_kiwo_wetter = df_umsatz.merge(df_kiwo, on='Datum').merge(df_wetter, on='Datum')
print(df_umsatz_kiwo_wetter.head())