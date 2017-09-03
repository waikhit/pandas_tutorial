import pandas as pd
import numpy as np

s = pd.Series(np.random.rand(5))


df = pd.DataFrame(s, columns = ['Column 1'])
df['Column 2'] = df['Column 1'] * 4
print(df)

print(df[df['Column 2'] <= 2])
print(df.describe())