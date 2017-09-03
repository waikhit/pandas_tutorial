import pandas as pd
import numpy as np

pd.Series(np.random.randn(5), index = ['a','b','c','d','e'])
s = pd.Series(np.random.randn(5))
print(s)

#Creating a dataframe

df = pd.Dataframe(s, columns = ['Column 1'])
df