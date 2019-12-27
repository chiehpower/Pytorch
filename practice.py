from __future__ import print_function
import torch

# 张量 Tensor（张量）类似于NumPy的ndarray，但还可以在GPU上使用来加速计算。
print("PyTorch Practice")
x = torch.rand(5, 3)
print(x)

x = torch.zeros(5,3, dtype=torch.long)
print(x)

x = torch.empty(5,3)
print(x)

x = torch.tensor([5.5,3])
print(x)




print(x.size())

# 运算

