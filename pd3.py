import pandas as pd
import numpy as np
t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
t1.iloc[1:,:2]=np.nan
print(t1)
print('\n')
t2=pd.isnull(t1)  #判断t1中是否有nan  相反的“notnull”
print(t2)
print('\n')
t2 = t1[pd.notnull(t1["W"])]  #W这一列不为nan的所有行
print(t2)
print('\n')

t3 = t1.dropna(axis=0,how="all")  #删除全为nan的那一行
print(t3)
print('\n')
t4 = t1.dropna(axis=0,how="any")  #删除有nan的那一行
print(t4)
print('\n')
#t5 = t1.dropna(axis=0,how="any",inplace=True)  #True表示替换t1
#print(t1)

d2 = [{"name":"xiaoming","age":18,"tel":10010},{"name":"xiaohong","tel":10000},{"name":"xiaowang","age":22}]
t5 = pd.DataFrame(d2)
print(t5)
print('\n')
t6 = t5.fillna(0) #填充nan为0
print(t6)
print('\n')
#t7 = t5.fillna(t5.mean())  #用均值填充
#print(t7)
#print('\n')
t5["age"]=t5["age"].fillna(t5["age"].mean())  #只有age这一列用均值填充
print(t5)

