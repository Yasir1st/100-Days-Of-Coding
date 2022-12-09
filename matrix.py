'''Membuat Matrix menggunakan numpy'''

import numpy as np
import os

os.system("cls")

def line():
    print("="*45)

line()
print("Matrix".center(25))
line()
list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a = {list_a}")
# print(list_a**2) <- ini akan gagal
line()

# Kita dapat langsung mengalikan semua komponen vektor sekaligus
print(f"vector_a = {vector_a}")
print(f"a pangkat 2 = {vector_a**2}")
print(f"a kali 5 = {vector_a*5}")
line()

# Membuat Matrix
matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}")
line()

# Matrix dengan value 0
zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")
line()

# Matrix dengan Value 1
ones_d = np.ones((2,2))
print(f"ones c = \n{ones_d}")
line()

# Menjulahkan Matrix
jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")
line()