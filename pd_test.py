import pandas as pd

data = [[3, 1, 3], [4, 3, 5.6]]
df = pd.DataFrame(data)

# 设置列名
df.columns = ['a', 'b', 'c']
# 设置行名
df.index = ['A', 'B']
# df.set_index('a')  # 把‘a’列作为index

#    a  b    c
# 0  3  1  3.0
# 1  4  3  5.6

# 对每列(series)应用函数
df.apply(sum)
#
# a    7.0
# b    4.0
# c    8.6

# 对series的每个元素应用函数
df.a.map(lambda x: x ** 2)

# 对dataframe每列的series的每个元素应用函数
df.applymap(lambda x: x ** 2)

# 直接遍历df，输出的是列名
for s in df:
    print(s)
# a
# b
# c


# 按行遍历
for s in df.iterrows():
    print(s)

# 按列遍历
for s in df.iteritems():
    print(s)

# 注意: append, apply, astype, 返回的都是拷贝

df2 = df.append({'a': 3, 'b': 2}, ignore_index=True)  # 用字典append时必须要ignore_index=True
#
#      a    b    c
# 0  3.0  1.0  3.0
# 1  4.0  3.0  5.6
# 2  3.0  2.0  NaN

df.append([4, 5], ignore_index=True)  # 不指定名称，会依次添加新行列
#      a    b    c    0
# 0  3.0  1.0  3.0  NaN
# 1  4.0  3.0  5.6  NaN
# 2  NaN  NaN  NaN  4.0
# 3  NaN  NaN  NaN  5.0


df3 = df2  # 引用,
df4 = df2.copy()

# loc下表访问，行列
print(df3.loc[2, 'c'])
df3.loc[2, 'c'] = 4
# 这种方式可以改变df3中的值， 注意df2也会变

# 注意：判断某项元素是非为空只能用np.isnan()
import numpy as np

print(type(df4.loc[2, 'c']))  # <class 'numpy.float64'>
print(df4.loc[2, 'c'] == float('nan'))  # False
print(df4.loc[2, 'c'] == np.nan)  # False
print(not bool(df4.loc[2, 'c']))  # False
print(np.isnan(df4.loc[2, 'c']))  # True

# 也可以用这种方式访问元素
print(df4['c'][2])
# 赋值也有效
df4['c'][2] = 88
