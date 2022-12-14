import os
os.system("cls")
 
def line():
    print("="*50)

line()
print("Yasir Diamond Store".center(50))
line()

print("Harga Paket Diamond ==> Rp.120.000")
line()
jumPaket = int(input("Masukkan Jumlah Paket Yang Dibeli : "))
line()

harga_per_paket = 120000
harga_total_paket = jumPaket*harga_per_paket

if(jumPaket >= 10 and jumPaket <= 19):
    diskon = 20/100
elif(jumPaket >= 20 and jumPaket <= 49):
    diskon = 30/100
elif(jumPaket >= 50 and jumPaket <= 69):
    diskon = 35/100
elif(jumPaket >= 70 and jumPaket <= 99):
    diskon = 40/100
elif(jumPaket >= 100):
    diskon = 50/100
else:
    diskon = 0

jumDiskon = harga_total_paket*diskon
jum_harga_setelah_diskon = harga_total_paket-jumDiskon

# Output
print(f"Harga Per Paket \t\t: Rp.{harga_per_paket}")
print(f"Harga Total Paket \t\t: Rp.{harga_total_paket}")
print(f"Harga Total Setelah Diskon \t: Rp.{jum_harga_setelah_diskon:.0f}")
print(f"Anda Hemat \t\t\t: Rp.{jumDiskon:.0f}")
line()

print("Terima Kasih Telah Berbelanja di Store Kami :)".center(50))
line()