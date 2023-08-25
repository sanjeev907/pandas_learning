import pandas as pd

# a = [1,3,2,57,45]
# b = pd.Series(a)
# print(b)

# a = [1,3,2,57,45]
# b = pd.Series(a)
# c = b.tolist()
# print(type(c))

# a = [2, 4, 6, 8, 10]
# b = [1, 3, 5, 7, 9]
# c = pd.Series(a)
# d = pd.Series(b)
# # e = c+d
# e = c*d
# print(e)

# a = [2, 4, 6, 8, 10]
# b = [1, 3, 5, 7, 10]
# c = pd.Series(a)
# d = pd.Series(b)
# e = c == d
# f = c > d
# g = c < d

# print(e,f,g)


# a = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# b = pd.Series(a)
# print(b)

import numpy as np

# a = [2, 4, 6, 8, 10]
# b = np.array(a)
# print(type(b))

# a = [2, 4, 6, 8, 10]
# b = pd.Series(a, dtype="float")
# print(b)


# a = {'Name':['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'], 'Marks':[98,89,99,87,90,83,99],' Gender':['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female']}
# b = pd.DataFrame(data= a)
# ser1 = b.ix[:,0]
# print(ser1)


# a = {'Name':['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'], 'Marks':[98,89,99,87,90,83,99],' Gender':['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female']}
# b = pd.DataFrame(a)
# c = b.sample(5)
# print(c)


a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv")
# b = a.head(7)
# b = a.tail(7)
# b = a.dtypes
# b = a.isnull().sum()
# b = a.columns
# b = a.info()
# b = a['values'].max()
# b = a['values'].min()
# b = a['values'].mean()
b = a['values'].median()
print(b)