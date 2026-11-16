import torch

a = torch.tensor(
    [[1, 2, 3],
     [4, 5, 6]],
    dtype=torch.int32
)

print("Tensor a:")
print(a)

print("Kích thước (shape):", a.shape)      
print("Số chiều (ndim):", a.ndim)          
print("Kiểu dữ liệu (dtype):", a.dtype)



a = torch.rand(3, 4)
b = torch.randn(3, 4)
c = torch.zeros(2, 3)
d = torch.ones(2, 3)
e = torch.eye(4)

print("a (torch.rand):", a)
print("b (torch.randn):", b)
print("c (torch.zeros):", c)
print("d (torch.ones):", d)
print("e (torch.eye):", e)

# Yêu cầu: Tạo Tensor 5x5 chứa toàn giá trị 10
# Cách 1: Dùng torch.full (gọn và chuẩn nhất)
tensor_10 = torch.full((5, 5), 10)

# Cách 2: Lấy tensor ones nhân với 10
# tensor_10 = torch.ones(5, 5) * 10

print("\nTensor 5x5 chứa toàn giá trị 10:")
print(tensor_10)