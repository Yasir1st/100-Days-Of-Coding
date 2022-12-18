import os
os.system("cls")

panjang = 83

def line():
    print("="*panjang)

def line2():
    print("-"*panjang)


line()
print("Program Kasir".center(panjang))
line()

print("""
---------------------------------------------
|                   MENU                    |
---------------------------------------------
|NO |        NAMA MAKANAN        |  HARGA   |
---------------------------------------------
|1. |Nasi ayam rica-rica         |25.000,00 |
|2. |Chicken burger              |25.000,00 |
|3. |Fish burger                 |20.000,00 |
|4. |Pisang coklat keju          |15.000,00 |
|5. |Roti ice cream              |15.000,00 |
|6. |Puding panggang             |20.000,00 |
|7. |Dark coklat                 |15.000,00 |
|8. |Jeruk panas/dingin          |18.000,00 |
|9. |Mochacinno milkshake        |20.000,00 |
|10.|Strawberry yakult milkshake |20.000,00 |
---------------------------------------------
""")

barang = []
harga = []
jumlah_barang = []
total_harga_barang = []
total_harga = 0

while True:
    line()

    KODE = int(input("masukkan kode barang \t: "))

    if KODE == 1:
        barang.append("Nasi ayam rica-rica")
        harga_barang = 25000
        harga.append(harga_barang)
    elif KODE == 2:
        barang.append("Chicken burger")
        harga_barang = 25000
        harga.append(harga_barang)
    elif KODE == 3:
        barang.append("fish burger")
        harga_barang = 20000
        harga.append(harga_barang)
    elif KODE == 4:
        barang.append("pisang coklat keju")
        harga_barang = 15000
        harga.append(harga_barang)
    elif KODE == 5:
        barang.append("Roti ice cream")
        harga_barang = 15000
        harga.append(harga_barang)
    elif KODE == 6:
        barang.append("puding panggang")
        harga_barang = 20000
        harga.append(harga_barang)
    elif KODE == 7:
        barang.append("Dark coklat")
        harga_barang = 15000
        harga.append(harga_barang)
    elif KODE == 8:
        barang.append("jeruk panas/dingin")
        harga_barang = 18000
        harga.append(harga_barang)
    elif KODE == 9:
        barang.append("mochacinno milkshake")
        harga_barang = 20000
        harga.append(harga_barang)
    elif KODE == 10:
        barang.append("Strawberry yakult milkshake")
        harga_barang = 20000
        harga.append(harga_barang)
    else:
        print("barang tidak terdaftar !!!")
        continue

    jumlah = int(input("jumlah pesanan \t\t: "))
    jumlah_barang.append(jumlah)
    total_belanja_perbarang = jumlah*harga_barang
    total_harga += total_belanja_perbarang
    total_harga_barang.append(total_belanja_perbarang)

    line()
    beli_barang_lain = input("Beli barang lain (y/n) \t: ").lower()
    if beli_barang_lain == "n" :
        line()
        break

line2()
print("Detail Pembelian".center(panjang))
line2()
print(f"| {'No':<3}| {'Nama Barang':<35}| {'Harga Barang':<13}| {'Jumlah':<7}| {'Total':<13} |")
line2()

banyak_barang = len(barang)
count = 0

while count <= banyak_barang-1:
    print(f"| {(count+1):<3}| {barang[count]:<35}| {harga[count]:<13}| {jumlah_barang[count]:<7}| Rp.{total_harga_barang[count]:<10} |")
    count += 1

line2()
print(f"| {'Total Belanja':^64}| Rp.{total_harga:<10} |")
line2()

while True:
    uang = int(input("Masukkan Total Uang Anda \t: Rp."))

    if(uang >= total_harga):
        kembalian = uang-total_harga
        break
    else:
        line2()
        print("Uang Anda Kurang, Coba Lagi !".center(panjang))
        line2()
        continue

line2()
print(f"| {'Kembalian':^64}| Rp.{kembalian:<10} |")
line()

print("|","Terima Kasih Telah Berkunjung".center(panjang-4),"|")

line()