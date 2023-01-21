print('''Item :
1. Teh Pucuk 4k
2. Tango     10k
3. Nabati    5k
4. Ichitan   9k
5. Pilus     2k
6. Oreo      8k
''')

jenisBarang = input("Masukkan Jenis Barang \t: ")
jumlaBarang = int(input("Masukkan Jumlah Barang \t: "))

if(jenisBarang == "1"):
    harga = 4000
elif(jenisBarang == "2"):
    harga = 10000
elif(jenisBarang == "3"):
    harga = 5000
elif(jenisBarang == "4"):
    harga = 9000
elif(jenisBarang == "5"):
    harga = 2000
elif(jenisBarang == "6"):
    harga = 8000
else:
    print("Barang Yang Di Pilih Tidak Tersedia")

totalBelanja = harga*jumlaBarang

print("Total Belanja \t\t: Rp. ",totalBelanja)

uang = int(input("Masukkan Pembayaran \t: Rp. "))

kembalian = uang-totalBelanja

print("Kembalian \t\t: Rp.",kembalian)