## Menghitung Luas dan Panjang serta menggambar persegi panjang

import os

# Fungsi Garis
def line():
    '''Fungsi Garis'''
    print("-"*40)
    return


# Fungsi Header
def header():
    '''Fungsi Header'''
    os.system('cls')
    line()
    print(f"{'Program Menghitung Luas, Panjang':^40}")
    print(f"{'Serta Menggambar Persegi':^40}")
    line()

# Fungsi Input
def input_user():
    '''Fungsi Input User'''
    panjang = int(input("Masukkan Nilai Panjang \t : "))
    lebar = int(input("Masukkan Nilai Lebar \t : "))
    line()
    return panjang,lebar

def luas_persegi_panjang(lebar,panjang):
    '''Fungsi Luas'''
    return panjang*lebar

def keliling_persegi_panjang(lebar,panjang):
    '''Fungsi Keliling''' 
    return 2*(panjang+lebar)

def gambar_persegi_panjang(lebar,panjang):
    '''Fungsi Gambar'''
    print(f"Gambar Persegi Panjang \t : {LUAS}\n")
    for i in range(1,lebar+1):
        print(f"{'* '*panjang}") 


while True:
    header()
    PANJANG,LEBAR = input_user()
    LUAS = luas_persegi_panjang(LEBAR,PANJANG)
    KELILING = keliling_persegi_panjang(LEBAR,PANJANG)

    print(f"Luas Persegi Panjang \t : {LUAS}")
    print(f"Keliling Persegi Panjang : {KELILING}")
    line()

    gambar_persegi_panjang(LEBAR,PANJANG)
    line()

    isContinue = input("Apakah Lanjut (y/n) \t : ")
    if isContinue == "n" :
        break

line()
print(f"{'Program Selesai':^40}")
line()