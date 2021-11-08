import numpy as np
import pandas as pd

df = pd.read_csv('savedrecs.csv')

df.Survey.value_counts(dropna=False)
df.N.value_counts().sum()
df.Relevant.value_counts(dropna=False)

df_relevant = df[(df.Relevant!='9')]
df_relevant = df_relevant[df.Relevant!='9(social distancing)']

