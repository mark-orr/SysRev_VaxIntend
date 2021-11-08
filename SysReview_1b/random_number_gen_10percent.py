import numpy as np
import pandas as pd

a = np.array(range(0,1114))+1
len_a = len(a)
s = int(0.10 * len_a)

l_nonordered = np.random.choice(a,size=s,replace=False)
print("random list")
print(l_nonordered)

l_ordered = np.sort(l_nonordered)
print("ordered random list")
print(l_ordered)
df_l_ordered = pd.DataFrame(l_ordered)
df_l_ordered.to_csv('pd.csv',index=False,header=False)
np.savetxt('np.csv',l_ordered)
#EOF
