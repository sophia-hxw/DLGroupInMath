import pandas as pd
import numpy as np
y={"sex":["men","women","men"],"age":[10,20,20],"name":["ls","ls","ww"]}
x1 = pd.DataFrame(y)
print(x1)
print('\n')
print(x1.loc[:,"sex"].mode())  #mode()求众数

x=pd.DataFrame(np.random.randn(3,3),index=list("ABC"))
print(x)
print('\n')
print(x.sum(axis=1))  #1是行 0是列
print(x.mean()) #默认按列操作
print(x.max(axis=1))