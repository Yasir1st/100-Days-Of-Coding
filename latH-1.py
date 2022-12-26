import os
os.system("cls")

def line():
    print(f"\n{'='*50} \n")

line()

# Pyramid Angka
baris = int(input("Masukkab Jumlah Baris Pyramid : "))
for i in range(1,baris+1):
    print(i*str(i))

line()

# Bilangan Prima
batas = int(input("Batas Bilangan Prima : "))

for i in range(1,batas+1):
    if(i == 3 or i == 2):
        print(i)
    elif(i == 1 or i % 2 == 0 or i % 3 == 0):
        pass
    else:
        print(i)

line()

# Reverse kalimat
kalimat = input("Masukkan Kalimat : ")

reversedKalimat = reversed(kalimat)

for i in reversedKalimat:
    print(i,end="")
print("")

line()

# Mengurutkan isi list berdasarkan tipe datanya
list_acak = [1,0.4,"Yasir",False,"Fatim",12,6.2,True]

list_int = []
list_float = []
list_str = []
list_bool = []

for typeData in list_acak:
    if(type(typeData) == int):
        list_int.append(typeData)
    if(type(typeData) == float):
        list_float.append(typeData)
    if(type(typeData) == str):
        list_str.append(typeData)
    if(type(typeData) == bool):
        list_bool.append(typeData)

list_int.sort()
list_float.sort()
list_str.sort()
list_bool.sort()

print(list_int+list_float+list_str+list_bool)

line()