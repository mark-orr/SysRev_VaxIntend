import numpy as np
import pandas as pd

df_3 = pd.read_csv('savedrecs-3.csv')
df_4 = pd.read_csv('savedrecs-4.csv')

df_3 = df_3[['Survey','N','Relevant','Rel_2']]
df_4 = df_4[['Survey','N','Relevant','Rel_2']]

df = pd.concat([df_3,df_4])

df.Survey.value_counts(dropna=False)
df.N.value_counts()
a = df.Relevant.value_counts(dropna=False)
a.to_csv('RelevantFromPandas.csv')

df.Rel_2.value_counts()
