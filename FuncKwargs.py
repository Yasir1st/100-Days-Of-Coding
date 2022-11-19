# **kwargs function
import os
os.system("cls")

def line():
    '''Line Function'''
    print("="*40)
    
line()
print("Kwargs".center(40))

# Fungsi Biasa
line()
def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Yasir",161,65)
line()

# Menggunakan **kwargs / data yang di inputkan di kwargs berupa dictionary
# Misalkan pada fungsi data(nama="Yasir") maka key nama , value Yasir
def data(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

data(nama="Yasir",tinggi=161,berat=65)
line()

# **kwargs with *args
def math(*args,**kwargs):
    '''Function Math'''
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output +=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")

    return output

hasil = math(1,2,3,4,option="tambah")
print(f"hasil jumlah {hasil}")
line()

hasil = math(1,2,3,4,option="kali")
print(f"hasil kali {hasil}")
line()