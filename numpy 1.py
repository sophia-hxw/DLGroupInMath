import numpy as np
dt = np.dtype(np.int32)  #dt = np.dtype('i4') 同样的效果
#print(dt)
#print(type(dt))

student = np.dtype([("name","S20"),("age","i4"),('marks','f4')])
#print(student)
#print(type(student))

arr = np.array([1,2,3,4,5]) #一维数组
#print(arr)
#print(type(arr))

arr2 = np.array([1,2,3,4,5,6,7,8,9,0],ndmin=2)  #维度为2
#print(arr2)

arr3 = np.array([1,2,3,4,5],dtype=float)  #浮点数  等同于dtype=‘f’
print(arr3)
#结构化数据类型
student = np.dtype([("name","S20"),("age","i4"),('marks','f4')])
arr4 = np.array([("xieyao",21,98.99),("mark",18,97.58)])
#print(arr4)

t1 = np.array([1,0,1,0,1],dtype=bool)
print(t1)
print(t1.dtype)

#调整数据类型
t2 = t1.astype("int8")
print(t2)
print(t2.dtype)