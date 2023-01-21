list_angka = [i for i in range(1,15) if i % 2 == 0]
print(list_angka)
def line():
    print("="*50)

def title(isi):
    print(isi)

line()
title("SOAL NO 1".center(50))
#Menampilkan semua element List
line()
title("Meampilkan Semua Element List :")
print("Angka Kelipatan 2 = ",list_angka)
line()

#Menghapus Element Ke 3 
title("Hapus Element Ke 3 :")
list_angka.pop(2)
print(list_angka)
line()

#Menyisipkan nilai 5 pada elemet ke 3
title("Menyisipkan Nilai 5 Ke Element Ke 3 :")
list_angka.insert(2,5)
print(list_angka)
line()

#Menampilkan 3 Elemet Terakhir Dari List
title("Menampilkan 3 Element Terakhir Dari List :")
list_angka = list_angka[-3:]
print(list_angka)
line()  

