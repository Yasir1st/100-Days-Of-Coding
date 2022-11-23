import os
os.system("cls")

line = lambda :print("="*44)

line()
print("Input Data Karyawan".center(44))
line()

nama = input("Nama Karyawan \t\t: ")
gaji = int(input("Gaji Pokok \t\t: Rp."))
jumlah_anak = int(input("Jumlah Anak \t\t: "))
statusNikah = input("Status Pernikahan (y/n) : ").lower()

# Tunjangan
tunjanganAnak = (gaji*5/100)*jumlah_anak
if(statusNikah == "y"):
    tunjanganIstri = gaji*2/100
else:
    tunjanganIstri = 0

gaji_sebelum_pajak = gaji+tunjanganAnak+tunjanganIstri

# Pajak
pajak = gaji_sebelum_pajak*10/100
gaji_bersih = gaji_sebelum_pajak-pajak

# output
line()
print("Data Gaji Karyawan".center(44))
line()
print(f"Nama Karyawan \t\t: {nama}")
print(f"Gaji Pokok \t\t: Rp.{gaji:,.0f}")
print(f"Tunjangan Istri \t: Rp.{tunjanganIstri:,.0f}")
print(f"Tunjangan Anak \t\t: Rp.{tunjanganAnak:,.0f}")
print(f"Total Tunjangan \t: Rp.{tunjanganAnak+tunjanganIstri:,.0f}")
print(f"Gaji Sebelum Pajak \t: Rp.{gaji_sebelum_pajak:,.0f}")
print(f"Total Pajak \t\t: Rp.{pajak:,.0f}")
print(f"Gaji Bersih \t\t: Rp.{gaji_bersih:,.0f}")
line()
print("Thankyou".center(44))
line()