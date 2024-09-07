import pandas as pd
a = [2,4,6,8,10,5]
series = pd.Series(a)
series+=5
print("The series of number after added 5 in each elements are:")
print(series)
mean = series.mean()
print("The mean of elements :")
print(mean)
stda = series.std()
print("The standard deviation of elements :")
print(stda)
ToList = series.to_list()
print("Convert series into list :")
print(ToList)
print(type(ToList))