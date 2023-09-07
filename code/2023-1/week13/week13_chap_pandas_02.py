# week13_chap_pandas_02.py

import pandas as pd


def square(data):
    return data * data


df = pd.DataFrame(
	[
		[4, 9, 10],
		[5, 38, 11],
		[6, 9, 12],
        [6, 9, 8]
        ], index=[1, 2, 3, 4], columns=['a', 'b', 'c']
	)


print(df)
print(df.iloc[:, [0,1]])
print(len(df))
print(df.shape)
print(df['b'])
print(df['b'].unique())
print(df.describe())
print(df['c'].sum())
print(df.apply(lambda x: x * x))
