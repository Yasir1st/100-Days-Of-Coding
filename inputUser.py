namaDepan = input("Masukkan nama depan : ")
namaBelakang = input("Masukkan nama belakang : ")
umur = int(input("Masukkan umur : "))
tinggi =  float(input("Masukkan tinggi badan : "))
beratBadan = float(input("Masukkan berat badan : "))
ukuranBaju = input("Masukkan ukuran baju : ")
statusPernikahan = input("Masukkan status Pernikahan : ")
noTelp = input("Masukkan no. telpon : ")

print("====================================")

print("Nama Depan =",namaDepan)
print("Nama Belakang =",namaBelakang)
print("Umur =",umur)
print("Tinggi Badan =",tinggi,"m")
print("Berat Badan =",beratBadan,"kg")
print("Ukuran Baju =",ukuranBaju)

if(statusPernikahan == "Sudah"):print("Status Pernikahan : Sudah Menikah")
else:print("Status Pernikahan : Belum Menikah")

print("No Telepon : ",noTelp)