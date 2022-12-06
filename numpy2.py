import numpy as np
arr = np.empty([3,2],dtype=int)
#print(arr)

arr2 = np.zeros(5,dtype=int)
arr3= np.zeros([3,2],dtype=[('x','i4'),('y','f')])
print(arr3)

arr4 = np.ones([3,2],dtype='i4')

arr5 = np.full(5,fill_value=1024)
print(arr5)

arr6 = np.eye(10,dtype=int)  #对角线为1，其他为0

arr7 = np.arrange(1,11,1) #1-10，步长为1

x=[1,2,3,4,5]
z=iter(x)
arr8 = np.fromiter(z,dtype='f')
print(arr8)

arr9 = np.linspace(1,10,10,dtype = 'i4')  #等差数列
arr10 = np.logspace(1.0,2.0,10)  #等比数列

