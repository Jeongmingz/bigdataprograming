# DataFrame
import pandas as pd
import numpy as np
import pickle


df: pd.DataFrame() = pickle.load(open('../parking_dataframe.pkl', "rb"))
df['date'] = df["date"].dt.strftime("%Y-%m-%d %H")
print(df.head())
# array1 = np.arange(1, 5)
# array2 = np.arange(5, 9)
#
# # 1
# df1 = pd.DataFrame(
# 	{'array1': array1,
# 	 'array2': array2,}
# 	)
#
# # 2
# df2 = pd.DataFrame(
# 	[array1, array2],
# 	index=['array1', 'array2']
# 	)
#
# # 3
# df3 = pd.DataFrame(
# 	{'array1': array1,
# 	 'array2': array2},
# 	index = pd.MultiIndex.from_tuples(
# 		[('f', 1), ('f', 2), ('b', 3), ('b', 4)], names=['location', 'index']
# 		)
# 	)
#
# print(df3)
# print(pd.melt(df1).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 4'))
#
# df1 = pd.DataFrame(
# 	{"a": [4, 5, 6],
# 	 "b": [7, 8, 9],
# 	 "c": [10, 11, 12]},
# 	index=[1, 2, 3])
#
# df2 = pd.DataFrame(
# 	{"e": [13, 14, 15],
# 	 "f": [16, 17, 18]},
# 	index=[1, 2, 3])
#
# np.arange()
#
# print(pd.concat([df1, df2], axis=0, ignore_index=False))  # concat function:(list, <Optional/ key arg> args=0)
# print(pd.concat([df1, df2], axis=1))
# print(pd.concat([df1, df2], axis=1, join='inner'))
# print()
#
