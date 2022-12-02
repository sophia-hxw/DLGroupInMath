import numpy as np
a = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
b = np.array([1,2,3])
c = a+b
#print(c)

bb = np.tile(b,(4,1))
#print(bb)
#print('\n')
#print(a+bb)

#迭代 np.nditer
a2 = np.arange(12)
a2.shape = (3,4)
print(a2)
print('\n')
for x in np.nditer(a2):
    print(x,end="，")
print("")
print('\n')
print(a2.T) #转置
print('\n')
for x in np.nditer(a2.T):
    print(x,end="，")
print('\n')

b2 = a2.T.copy(order="C")  #order=F 列优先 C 行优先
print(b2)
print('\n')
for x in np.nditer(b2):
    print(x,end="，")
print('\n')

a3 = np.arange(12)
a3.shape = (3,4)
print(a3)
print('\n')
for x in np.nditer(a3,order="F",op_flags=["readwrite"]): #op_flags可以改读
    x[...] = x*2
print('\n')
print(a3)

a4 = np.arange(12)
a4.shape = (3,4)
print(a4)
print('\n')
for x in np.nditer(a4,flags=["external_loop"],order="F"): #不是单个数据，而是变成一维数组
    print(x,end="，")
print("")

a5 = np.arange(12)
a5.shape = (3,4)
b3 = np.arange(1,5)
for x,y in np.nditer([a5,b3]):
    print("%d:%d"%(x,y),end="，")

