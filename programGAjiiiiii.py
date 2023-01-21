pekerjaan = input("Masukkan Jenis Pekerjaan \t: ").upper()
gaji = int(input("Masukkan gaji \t\t\t: "))

if(gaji >= 5000000):
    pajak = gaji*0.1
elif(gaji >= 3000000):
    pajak = gaji*0.05
else:
    pajak = 0

gajiKotor = gaji-pajak

if(pekerjaan == "PNS"):
    pajakTambahan = gajiKotor*0.05
else:
    pajakTambahan = 0

print(f"Nama Pekerjaan : {pekerjaan}")
print(f"Pajak : {pajak}")
print(f"Gaji Kotor : {gajiKotor}")
print(f"Pajak Tambahan : {pajakTambahan}")
print(f"Gaji Bersih    : {gajiKotor-pajakTambahan}")