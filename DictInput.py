import datetime as dt
import os
os.system("cls") # Jika Menggunakan Mac maka "cls" diganti "clear"

def line():
    print("-"*44)
# Program Input Dictionary

# Template Data Mahasiswa
template_mahasiswa = {
    "Nama":"Nama",
    "NIM":"D0000000",
    "Tanggal_Lahir":dt.datetime(1111,1,11),
    "SKS_Lulus":0
}

mahasiswa = dict.fromkeys(template_mahasiswa.keys())
# Input
line()
print(f"{'Selamat Datang':^44}")
line()
print(f"{'Input Data Mahasiswa':^44}")
line()
mahasiswa["Nama"] = input("Nama Mahasiswa \t: ")
mahasiswa["NIM"] = input("NIM Mahasiswa \t: ")
TANGGAL = int(input("Tanggal Lahir \t: "))
BULAN = int(input("Bulan Lahir \t: "))
TAHUN = int(input("Tahun Lahir \t: "))
mahasiswa['Tanggal_Lahir'] = dt.datetime(TAHUN,BULAN,TANGGAL)
mahasiswa["SKS_Lulus"] = input("SKS Lulus\t: ")
line()
print(f"{'Hasil Input':^44}")
line()
print(mahasiswa)
line()