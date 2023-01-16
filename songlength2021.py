import pandas as pd
import numpy as np
df = pd.read_csv("spotify_top50_2021.csv", encoding = 'latin-1')
df2 = df[['duration_ms',]]



df2['duration_s'] = (df2['duration_ms'] / 1000)

print(df2.head())


sum2021 = 0
for i in range(len(df2)):
    sum2021 += df2.loc[i, 'duration_s']
    avg2021 = round(sum2021 / 50, 2)

print(avg2021)    

