import os
os.system("cls")

line = lambda :print("="*44)

line()
print("Input Data Karyawan".center(44))
line()

# Input Data
nama = input("Nama Karyawan \t\t: ")
golongan = input("Golongan(I/II/III) \t: ").upper()
lamaKerja = int(input("Lama Bekerja(Tahun) \t: "))

# Gaji Pokok Berdasarkan Golongan
if(golongan == "I"):
    gaji = 4000000
elif(golongan == "II"):
    gaji = 7000000
elif(golongan == "III"):
    gaji = 10000000
else:
    print("Tidak Termasuk Golongan Manapun")

# Bonus Gaji Berdasarkan Lama Kerja
if(lamaKerja > 5):
    bonus = lamaKerja*100000
else:
    bonus = 0

# Output
line()
print("Detail Data Karyawan".center(44))
line()
print(f"Nama Karyawan \t\t: {nama}")
print(f"Golongan \t\t: {golongan}")
print(f"Gaji Pokok \t\t: Rp.{gaji:,.0f}")
print(f"Bonus Gaji \t\t: Rp.{bonus:,.0f}")
print(f"Gaji Bersih \t\t: Rp.{gaji+bonus:,.0f}")
line()
print("Thankyou".center(44))
line()