import torch

x_data = torch.Tensor([[1.0],[2.0],[3.0]])
y_data = torch.Tensor([[2.0],[4.0],[6.0]])

class LinearModel(torch.nn.Module):
    def __init__(self): #构造函数
        super(LinearModel, self). __init__()
        self.linear = torch.nn.Linear(1, 1) #构造对象，并说明输入输出的维数，第三个参数默认为true，表示用到b

    def forward (self,x):
        y_pred = self.linear(x) #可调用对象，计算y=wx+b
        return y_pred
model = LinearModel()#实例化模型

criterion = torch.nn.MSELoss(reduction='sum') #MSE:平均均方误差 sum:误差求和
#model.parameters()会扫描module中的所有成员，如果成员中有相应权重，那么都会将结果加到要训练的参数集合上
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  #lr为学习速率
for epoch in range (1000): #循环迭代
    y_pred = model (x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss)
    optimizer.zero_grad() #梯度清零
    loss.backward() #反向传播，计算梯度
    optimizer.step() #update 参数更新 即更新w和b的值
print('w = ', model.linear.weight.item())
print('b = ', model.linear.bias.item())
x_test = torch.Tensor([[4.0]])
y_test = model(x_test)
print('y_pred = ',y_test.data)
