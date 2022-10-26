angka_kelipatan2 = [2,4,6,8,10,12,14]

def line():
    print("="*50)

def title(isi):
    print(isi)

line()
title("                     SOAL NO 1")
#Menampilkan semua element List
line()
title("Meampilkan Semua Element List :")
print("Angka Kelipatan 2 = ",angka_kelipatan2)
line()

#Menghapus Element Ke 3
title("Hapus Element Ke 3 :")
angka_kelipatan2.pop(2)
print(angka_kelipatan2)
line()

#Menyisipkan nilai 5 pada elemet ke 3
title("Menyisipkan Nilai 5 Ke Element Ke 3 :")
angka_kelipatan2.insert(2,5)
print(angka_kelipatan2)
line()

#Menampilkan 3 Elemet Terakhir Dari List
title("Menampilkan 3 Element Terakhir Dari List :")
angka_kelipatan2 = angka_kelipatan2[-3:]
print(angka_kelipatan2)
line()  

