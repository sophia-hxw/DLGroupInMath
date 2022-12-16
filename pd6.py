import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,10,(3,3)),
                  index=["a","b","c"],
                  columns=["one","two","three"])  #0-10的随机数 三行三列
print(df)
print('\n')
print("每一行的和\n",df.sum(axis=1))
print("每一行的均值\n",df.mean(axis=1))
print("每一行的众数\n",df.mode(axis=1))
print("每一行的下四分位数\n",np.quantile(df,0.25,axis=1))
print("每一行的最大值\n",df.max(axis=1))
print("每一行的标准差\n",df.std(axis=1))
print("每一行的累加值\n",df.cumsum(axis=1))
