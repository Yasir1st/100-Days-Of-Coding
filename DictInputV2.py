import datetime as dt
import os
import string
import random

def line():
    print("-"*51)
# Program Input Dictionary

# Template Data Mahasiswa
template_mahasiswa = { 
    "nama":"nama",
    "nim":"D0000000",
    "tanggal_lahir":dt.datetime(1111,1,11),
    "sks_lulus":0
}

data_mahasiswa = {}
# Input
while True:
    os.system("cls")
    line()
    print(f"{'Selamat Datang':^44}")
    line()
    print(f"{'Input Data Mahasiswa':^44}")
    line()
    mahasiswa = dict.fromkeys(template_mahasiswa.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa \t: ")
    mahasiswa['nim'] = input("NIM Mahasiswa \t: ")
    TANGGAL = int(input("Tanggal Lahir \t: "))
    BULAN = int(input("Bulan Lahir \t: "))
    TAHUN = int(input("Tahun Lahir \t: "))
    mahasiswa['tanggal_lahir'] = dt.datetime(TAHUN,BULAN,TANGGAL)
    mahasiswa['sks_lulus'] = input("SKS Lulus\t: ")
    line()

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    
    print(f"\n{'KEY':<6} {'NIM':<10} {'Nama':<17} {'SKS':<3} {'Tanggal_Lahir':<10}")
    line()
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['tanggal_lahir'].strftime("%x")

        print(f"\n{KEY:<6} {NIM:<10} {NAMA:<17} {SKS:<3} {LAHIR:<10}") 
    line()
        
    print("\n")
    is_done = input("Input Lagi Bro (y/n) ?")
    if is_done == "n":
        break