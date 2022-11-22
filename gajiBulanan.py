import os

line = lambda :print("="*40)

os.system("cls")
line()
print("Geji Bersih Bulanan".center(40))
line()

# Input 
gaji = int(input("Gaji Bulanan \t\t: Rp."))
jumlah_alfa = int(input("Jumlah Alfa \t\t: "))
line()

# Kondisi
if(jumlah_alfa > 5):
    potonganGaji = jumlah_alfa*25000
    gaji_sebelum_pajak = gaji-potonganGaji
    pajak = gaji_sebelum_pajak*2.5/100
    gaji_bersih = gaji_sebelum_pajak-pajak
    print(f"Gaji Bersih Karyawan \t: Rp.{gaji_bersih:.2f}")
else:
    pajak = gaji*2.5/100
    gaji_bersih = gaji-pajak
    print(f"Gaji Bersih Karyawan \t: Rp.{gaji_bersih:.2f}")
line()
 