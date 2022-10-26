def line():
    print("="*64)

line()
print("Input List".center(64))
line()
start = int(input("Mulai Dari Angka : "))
stop = int(input("Sampai Angka : "))
stop += 1
kelipatan = int(input("Dengan Kelipatan : "))

list_bilangan = [i for i in range(start,stop) if i % kelipatan == 0]

#Menampilkan Isi Dari List
line()
print("List Bilangan :",list_bilangan)


#Menghitung Jumlah Elemet List 
line()
jumlah_element = len(list_bilangan)
print("Jumlah Element List : ",jumlah_element)
line()

#Menjumlahkan Seluruh Element List
jumlah_nilai = sum(list_bilangan)
print("Hasil Penjumlahan Semua Element List : ",jumlah_nilai)
line()

#Print Item Terakhir Pada List
print("Item Terakhir Dalam List : ",list_bilangan[-1])
line()

#Print List Dalam Urutan Terbalik 
list_bilangan.reverse()
print("List Bilangan Urutan Terbalik : ",list_bilangan)
line()

#Tampilkan Yes jika mengandung angka 7 , jika tidak maka tampilkan NO
cek_angka_7 = 7 in list_bilangan
if(cek_angka_7 == True):
    print("Apakaha Terdapat Nilai 7 Pada List : Yes")
else:
    print("Apakaha Terdapat Nilai 7 Pada List : No")
line()
    
#Tampilkan Bilangan Ke 5 Dalam List
print("Bilangan Ke 5 Dalam List : ",list_bilangan[4])
line()

#Hapus Element Pertama Dan Terakhir Lalu Urutkan List
list_bilangan.pop()
list_bilangan.pop(0)
print("Urutan Item List Setelah Element Pertama dan Terakhir Di Hapus:")
list_bilangan.reverse()
print(list_bilangan)
line()