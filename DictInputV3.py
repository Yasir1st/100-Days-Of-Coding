import datetime as dt
import os
import random
import string

# Fungsi Garis
def line():
    print("="*98)
    return

# Template Data Buku
template_buku = {
    "judul":"judul",
    "penulis":"yasir",
    "penerbit":"PT. Indo Sentosa",
    "terbit": dt.datetime(2000,1,1)
}

data_buku = {}

def header():
    '''Header'''
    os.system('cls')
    line()
    print("Program Input Data Buku".center(98))
    line()

def table(key,judul,penulis,penerbit,terbit):
    print(f"| {key:<7} | {judul:<20} | {penulis:<20} | {penerbit:<20} | {terbit:<15} |")

while True:
    header()
    buku = dict.fromkeys(template_buku.keys())
    buku['judul'] = input("Judul Buku \t: ")
    buku['penulis'] = input("Penulis Buku \t: ")
    buku['penerbit'] = input("Penerbit Buku \t: ")
    TANGGAL = int(input("Tanggal Terbit \t: "))
    BULAN = int(input("Bulan Terbit \t: "))
    TAHUN = int(input("Tahun Terbit \t: "))
    buku['terbit'] = dt.datetime(TAHUN,BULAN,TANGGAL)
    line()
    
    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_buku.update({KEY:buku})

    table("SERI","JUDUL","PENULIS","PENERBIT","TANGGAL TERBIT")
    line()
    for buku in data_buku :
        KEY = buku
        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        PENERBIT = data_buku[KEY]['penerbit']
        TERBIT = data_buku[KEY]['terbit'].strftime("%x")
        table(KEY,JUDUL,PENULIS,PENERBIT,TERBIT)
    line()

    isContinue = input("Tambah Lagi Gan (y/n) \t: ")
    line()
    
    if isContinue == "n":
        print(f"{'Program Selesai':^82}")
        line()
        break