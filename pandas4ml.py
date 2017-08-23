import numpy as np
import pandas as pd

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

dates = pd.date_range('20170823', periods=6)
print(dates)
dates1 = pd.date_range('20170823', '20170903')
print(dates1)

df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df1)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20170823'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float64'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)
print(df2.index, df2.columns, df.values, sep='\n')
print(df2.describe())

df3 = df2.T
print(df3)

df4 = df2.sort_index(axis=1, ascending=False)
print(df4)

df5 = df2.sort_values(by='E')
print(df5)



