import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
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

# selection
print(df['a'], df.a, df[0:3], df['20170823': '20170827'], sep='\n')

# select by label: loc
print(df.loc['20170824'])
print(df.loc[:, ['a', 'c']])

# select by position: iloc
print(df.iloc[3], df.iloc[3: 5, 1: 3], df.iloc[[1, 3, 4], 1: 3], sep='\n')

# mixed selection: ix
print(df.ix[1: 3, ['a', 'd']])

# boolean indexing
print(df[df.a > 0.5])

df.iloc[2, 2] = 110
df.loc['20170823', 'a'] = 111
df.a[df.a < 0.5] = 0
print(df)

df['e'] = np.nan
df['f'] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
print(df)

# nan
print(df.dropna(axis=1, how='any'))  # how={'any', 'all'}
print(df.fillna(value=0))
print(df.isnull())
print(np.any(df.isnull() == True))

# IO
# data = pd.read_xxx('XXX.xxx')
# data.to_xx('XX.xx')


# concatenating
Df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
Df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
Df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
print(Df1, Df2, Df3, sep='\n')
res = pd.concat([Df1, Df2, Df3], axis=0, ignore_index=True)
print(res)

# join
Df4 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
Df5 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(Df4, Df5, sep='\n')
res1 = pd.concat([Df4, Df5], join='outer')
res2 = pd.concat([Df4, Df5], join='inner')
print(res1, res2, sep='\n')

# join_axes
res3 = pd.concat([Df4, Df5], axis=1, join_axes=[Df4.index])
print('res3: ', res3, sep='\n')

# append
res4 = Df1.append([Df2, Df3], ignore_index=True)
print('res4: ', res4, sep='\n')

res5 = res.append(pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), ignore_index=True)
print('res5: ', res5, sep='\n')

# merge
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
res6 = pd.merge(left, right, on='key')
print('res6: ', res6, sep='\n')

# consider two keys
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left1, right1, sep='\n')
res7 = pd.merge(left1, right1, on=['key1', 'key2'], how='inner')  # how={'left', 'right', 'outer', 'inner'}
print('res7: ', res7, sep='\n')

res8 = pd.merge(left1, right1, on=['key1', 'key2'], how='outer')
print('res8: ', res8, sep='\n')

res9 = pd.merge(left1, right1, on=['key1', 'key2'], how='left')
print('res9: ', res9, sep='\n')

res10 = pd.merge(left1, right1, on=['key1', 'key2'], how='right')
print('res10: ', res10, sep='\n')

res11 = pd.merge(left1, right1, on=['key1', 'key2'], how='outer', indicator=True)
print('res11: ', res11, sep='\n')

res12 = pd.merge(left1, right1, on=['key1', 'key2'], how='outer', indicator='indicator_columns')
print('res12: ', res12, sep='\n')

# left_index  right_index
res13 = pd.merge(Df4, Df5, how='outer', left_index=True, right_index=True)
print('res13: ', res13, sep='\n')

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res14 = pd.merge(boys, girls, on='k', how='outer', suffixes=['_boy', '_girl'])
print(pd.merge(boys, girls, on='k', how='outer'))
print('res14: ', res14, sep='\n')
print(pd.merge(Df4, Df5, how='outer', left_index=True, right_index=True, suffixes=['_left', '_righr']))

# panda plot
# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
data.plot()

# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=['a', 'b', 'c', 'd'])
data = data.cumsum()
data.plot()
# plot methods:
# bar, hist, box, kde, area, scatter, hexbin, pie
ax = data.plot.scatter(x='a', y='b', color='DarkBlue', label='Class 1')
data.plot.scatter(x='a', y='c', color='DarkGreen', label='Class 2', ax=ax)
plt.show()
