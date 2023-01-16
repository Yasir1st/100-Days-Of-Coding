import os
os.system("cls")

def line():
    print("="*50)

line()
print("YZR Store".center(50))
line()

print('''Barang yang tersedia :
1. Kaos  Rp. 35.000
2. Kemeja Rp. 100.000
3. Celana Rp 50.000

Ukuran yang tersedia S, M, L, XL, XXL''')
line()

# harga awal 
harga_kaos = 35000
harga_kemeja = 100000
harga_celana = 50000

barang = int(input("Barang Yang di Beli(1/2/3) \t: "))
ukuran = input("Ukuran \t\t\t\t: ").upper()

# Pengecekan Panjang/Pendek
if barang == 3:
    ket = input("Celana (Panjang/Pendek) \t: ").lower()
else:
    ket = input("Lengan (Panjang/Pendek) \t: ").lower()

# Tambahan Harga Atau Pendek
if ket == "panjang":
    harga_kaos += 5000
    harga_kemeja += 10000
    harga_celana += 5000
else:
    harga_kaos += 0
    harga_kemeja += 0
    harga_celana += 0

# Tambahan Harga Berdasarkan ukuran
if ukuran == "XXL":
    harga_kaos += 10000
    harga_kemeja += 15000
    harga_celana += 10000
elif ukuran == "XL":
    harga_kaos += 5000
    harga_kemeja += 10000
    harga_celana += 5000
else:
    harga_kaos += 0
    harga_kemeja += 0
    harga_celana += 0

line()
if barang == 1:
    print(f"Total Harga \t\t\t: {harga_kaos}")
elif barang == 2:
    print(f"Total Harga \t\t\t: {harga_kemeja}")
else:
    print(f"Total Harga \t\t\t: {harga_celana}")

line()
print("Terima Kasih".center(50))
line()