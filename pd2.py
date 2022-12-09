import pandas as pd
import numpy as np
t = pd.DataFrame(np.arange(12).reshape(3,4))
print(t)
print('\n')

#横向索引 index 0轴 axis=0
#纵向索引 columns 1轴 axis=1

t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
print(t1)
print('\n')
print(t1.loc["a","Z"])  #a行Z列
print('\n')
print(t1.loc["a",:])
print('\n')
print(t1.loc[:,"Y"])
print('\n')
print(t1.loc[["a","c"],:])
print('\n')
print(t1.loc["a":"c",:])  #包括c这一行 冒号在loc里面是闭合的
print('\n')
print(t1.iloc[1,:])#第2行的内容
print('\n')
print(t1.iloc[[0,2],[2,1]])  #第一行和第三行，第三列和第二列
print('\n')
print(t1.iloc[:,[2,1]]) #第三列和第二列
print('\n')

d1 = {"name":["xiaoming","xiaohong"],"age":[18,30],"tel":[10086,10010]}
t2 = pd.DataFrame(d1)
#print(t2)
#print('\n')

d2 = [{"name":"xiaoming","age":18,"tel":10010},{"name":"xiaohong","tel":10000},{"name":"xiaowang","age":22}]
t3 = pd.DataFrame(d2)
#print(t3)
#print('\n')

