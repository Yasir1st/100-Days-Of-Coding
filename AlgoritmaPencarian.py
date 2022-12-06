import os
os.system("cls")

def line():
    print("="*50)

line()
print("Algoritma Pencarian".center(50))
line()
inputLawal = int(input("Larik Mulai Dari \t= ")) 
inputLakhir = int(input("Larik Berakhir Pada \t= "))
kelipatan = int(input("Kelipatan \t\t= "))
line()
larik = [i for i in range(inputLawal,inputLakhir+1) if i % kelipatan == 0]

x = int(input("Masukkan Nilai Yang di Cari \t= "))

i = 0
line()
print(f"Larik = {larik}")
line()

while True:
    if(x > larik[-1]):
        print(f"Nilai {x} tidak ditemukan, idx = -1")
        break
    elif(larik[i] == x):
        print(f"Nilai {x} ditemukan, idx = {larik.index(x)}")
        break
    else:
        i += 1
        continue

line()