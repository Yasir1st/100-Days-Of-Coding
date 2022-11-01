def line():
    print("-"*44)

data_0 = [1,2,3]
data_1 = [4,5,6]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()
line()
print("Mengunakan Copy".center(44))
line()
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
line()
# mengambil data dari nested list

data = data_2D[1][0]
print(f"data = {data}")
line()
# address semuanya

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")
line()
print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")
line()
data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
line()
# kita gunakan deepcopy

from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)
print("Mengunakan Deep Copy".center(44))
line()
print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

line()
print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")
line()

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")
line()