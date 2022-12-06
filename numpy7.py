import numpy as np

def fill_ndarray(t1):
    for i in range(t1.shape[1]): #遍历每一列
        temp_col=t1[:,i] #当前的一列
        nan_num=np.count_nonzero(temp_col!=temp_col) #统计nan的个数
        if nan_num!=0: #不为0，说明当前这一列中有nan
           temp_not_nan_col=temp_col[temp_col==temp_col] #当前一列不为nan的数组
       #选中当前为nan的位置，把值赋值不为nan的均值
           temp_col[np.isnan(temp_col)]=temp_not_nan_col.mean() #等号后面为均值
    return t1

if __name__=='__main__':
    t1 = np.arange(12).reshape(3, 4).astype("float")
    t1[1, 2:] = np.nan
    print(t1)
    print('\n')
    t1=fill_ndarray(t1)
    print(t1)