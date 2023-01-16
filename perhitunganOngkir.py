import os
os.system("cls")

def line():
    print("="*50)

# menu input ===> POV Penerima

line()
print("Program Perhitungan Ongkir".center(50))
line()

jarak = int(input("Jarak Pengiriman(KM) \t: "))
metode_pembayaran = input("Metode Pembayaran \t: ").lower()

biaya_per_KM = 3000
total_ongkir = jarak*biaya_per_KM

if jarak > 50:
    diskon = 0.1
elif jarak > 30:
    diskon = 0.05
else:
    diskon = 0

total_diskon = total_ongkir*diskon
total_sebelum_metode = total_ongkir-total_diskon

if metode_pembayaran == "pay later":
    tambahan = total_sebelum_metode*5/100
    total_keseluruhan = total_sebelum_metode+tambahan
elif metode_pembayaran == "ewallet":
    diskonAgain = total_sebelum_metode*2/100
    total_keseluruhan = total_sebelum_metode-diskonAgain
else:
    total_keseluruhan = total_sebelum_metode
line()
print(f"Jarak Pengiriman \t: {jarak} km")
print(f"Metode Pembayaran \t: {metode_pembayaran}")
print(f"Total Pembayaran \t: Rp.{total_keseluruhan}")
line()
print("Thank You".center(50))
line()
