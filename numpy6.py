import numpy as np
t1=np.arange(0,12).reshape(2,6)
print(t1)
print('\n')
t2=np.arange(12,24).reshape(2,6)
print(t2)
print('\n')
t3=np.vstack((t1,t2))  #竖直拼接
print(t3)
print('\n')
t4=np.hstack((t1,t2))  #水平拼接
print(t4)
print('\n')

t=np.arange(12,24).reshape(3,4)
t[[1,2],:]=t[[2,1],:] #行交换
print(t)
print('\n')
t[:,[0,2]]=t[:,[2,0]] #列交换
print(t)
