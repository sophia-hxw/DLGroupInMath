import pandas as pd
t = pd.Series([1,2,31,12,3,4])
print(t)
print(type(t))
print('\n')

t2 = pd.Series([1,23,2,2,1],index=list("abcde"))
print(t2)
print('\n')
t4 = t2.astype(float)
print(t4)
print('\n')

temp_dict={"name":"xiaohong","age":18,"tel":10086} #字典
print(temp_dict)
print('\n')
t3 = pd.Series(temp_dict)
print(t3)
print('\n')
#索引
print(t3["age"])
print(t3[2]) #第3行
print(t3[:2])  #前2行
print('\n')
print(t3[[1,2]]) #第2行和第3行
print('\n')

print(t[t>4])
print('\n')

print(t3.index)#键
for i in t3.index:
    print(i)
print(type(t3.index))
print(len(t3.index))
print(list(t3.index)) #list转换成列表
print(list(t3.index[:2])) #提取列表的前两个
print('\n')
print(t3.values)#值
print('\n')

s = pd.Series(range(5))
print(s.where(s>0))  #<=0的变成NaN
print('\n')
print(s.mask(s>0)) #>0的变成NaN
print('\n')
print(s.where(s>1,10)) #<=1的变成10
print('\n')

