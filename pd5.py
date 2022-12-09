import pandas as pd
import numpy as np
dic = {
    "省份":["广东","广东","江苏","浙江","江苏","浙江"],
    "城市":["深圳","广州","苏州","杭州","南京","宁波"],
    "人口":[22286,21500,17319,12556,11715,9846],
    "GDP":[1090,1404,1065,919,827,788]}
df = pd.DataFrame(dic)
print(df)
print('\n')
#创建一个分组对象
group = df.groupby("省份")
#对各省GDP,人口数据进行求平均值
avg = group.mean()
print(avg)
print('\n')
#对各省GDP，人口数据求和
total = group.sum()
print(total)
print('\n')
#对各省GDP，人口数据求最值
max = group.max()
min = group.min()
print(max)
print('\n')
print(min)
#计算各省的人均GDP，精确到两位小数
avgpro = (total["GDP"]/total["人口"]).round(2)
print(avgpro)
print('\n')
#计算各列的中位数和标准差
median = group.median()
std = group.std()
print(median)
print('\n')
print(std)
print('\n')


