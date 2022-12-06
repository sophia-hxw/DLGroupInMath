import numpy as np
arr = np.arange(10)
s = slice(2,7,2)
#print(arr[s])  # 从索引2开始到7结束（不包含7），间隔为2
#strat:stop:step
arr2 = arr[2:7:2]
#print(arr2)

arr3 = np.arange(15)
arr3.shape = (5,3)
#print(arr3)
#print(arr3[ ,1]) #第2列元素
#print(arr3[1]) #第2行元素
#print(arr3[[1,3]])  #第2行和第4行元素
#print(arr3[ ,1:]) #第二列及剩下的所有元素

#整数数组索引
arr4 = np.arange(9)
arr4.shape = (3,3)
#print(arr4)
#print(arr4[[0,1,2],[0,1,0]]) #0,0 1,1 2,0

#行索引是0,0 3,3 列索引是0,2 0,2
arr5 = np.arange(12)
arr5.shape = (4,3)
#print(arr5)
#print('\n') #空行
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
arr6 = arr5[rows,cols]
#print('这个数组的四个角的元素是：')
#print(arr6)
#print(arr5[1:3,1:3])  #行1-2 列1-2

#布尔索引
arr7 = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
#print(arr7[arr7>5]) #大于5的元素
#arr7[arr7<5]=0  #小于5的变成0
t1 = np.where(arr7<=5,10,20)  #把小于5的变成10，其他的变成20
#print(t1)

t2 = arr7.clip(5,8)  #clip裁剪 小于5的变成5，大于8的变成8
#print(t2)

arr8 = np.array([np.nan,1,2,np.nan,3,4,5])  #用~来过滤nan
print(arr8[~np.isnan(arr8)])

