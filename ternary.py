import os
os.system("cls")

# Membuat Pengecekan ganjil / genap

# Jika Menggunakan Percabangn Biasa 
angka = 6

if(angka % 2 == 0):
    print("Genap")
else:
    print("Ganjil")

# Jika menggunakan Ternary Operator maka 
number = 8
cek = "Genap" if number % 2 == 0 else "Ganjil"
print(cek)

# Operator Ternary ini hanya menampung 3 operand saja tidak kurang dan tidak lebih