#Pandas works with dataframes. Dataframe is a spreadsheet. Why use python over excel. Excel is slow
import pandas as pd
import datetime
import pandas.io.data as web
import matlablib.pyplot as plt
from matlablib import style

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = web.DataReader('XOM', 'google', start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()
