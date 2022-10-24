def space():
    print(" ")
space()
###Operator Method String

#Menghitung banyak karakter Count()
name = "Karina Aespa"
panjang_nama = name.count("a") #hasilnya int
print("Banyak karakter a di nama " + name + " = " + str(panjang_nama))
space()

##Merubah Case dari String(Uppercase/lowercase)
#to upper
enak = "masisseoyo!!"
enak = enak.upper()
print(enak)

#to lower
thanks = "KAMSAHAMMIDA!"
thanks = thanks.lower()
print(thanks)
space()

##Pengecekan dengan isX Method
#pengecekan lower and upper case
cantik = "kirei"
apakah_lower = cantik.islower() #hasilnya boolean
apakah_upper = cantik.isupper() #hasilnya boolean
print("Apakah kata " + cantik + " adalah lowercase = " + str(apakah_lower))
print("Apakah kata " + cantik + " adalah uppercase = " + str(apakah_upper))
space()

#isalpha() <-- untuk mengecek apakah semuanya huruf
#isdecimal <-- untuk  mengecek apakah semuanya angka
#isalnum <-- untuk mengecek apakah terdiri dari angka dan huruf
#isspace() <-- untuk mengecek apakah sting kosong(spasi, tab, newline(\n))

#istitle() <-- untuk mengecek apakah semua katanya dimulai dari huruf besar
judul = "Big Mouth"
cek_judul = judul.istitle() #hasilnya boolean
print(judul,"is tittle = ",str(cek_judul))

judul2 = "Business proposal"
cek_judul = judul2.istitle() #hasilnya boolean
print(judul2,"is tittle = ",str(cek_judul))
space()

##cek komponen startswith() and endswith()
kalimat = "janeun yasir nmida"
cek_start = kalimat.startswith("janeun")
print("apakah kalimat ",kalimat," dimula dari kata janeun = ",str(cek_start))
cek_end = kalimat.endswith("yasir")
print("apakah kalimat ",kalimat," diakhiri oleh kata yasir = ",str(cek_end))
space()

##Penggabungan dan pemisahan komponen join() and split()
pisah = ["Indonesia","no","karakimashita"]
gabungan = " ".join(pisah)
gabungan2 = "-".join(pisah)

print("Normal = ",pisah)
print("Gabungan 1 = ",gabungan)
print("Gabungan 2 = ",gabungan2)
space()

gabung = "I Will Shutdown You"
gabung2 = "I#Will#Shutdown#You"
pisahkan = gabung.split()
pisahkan2 = gabung2.split('#')

print("Normal = ",gabung)
print("Pisah = ",pisahkan)

print("Normal = ",gabung2)
print("Pisah = ",pisahkan2)
space()

##Alokasi karakter rjust(), center(), ljust()
kanan = "kanan".rjust(15)
print("'"+kanan+"'")

tengah = "tengah".center(15)
tengah2 = "tengah".center(15,"=")
print("'"+tengah+"'")
print("'"+tengah2+"'")

kiri = "kiri".ljust(15)
print("'"+kiri+"'")
space()

##kebalikan dari center()/ menghilangkan tanda di alokasi karakter
tengah3 = "Karina".center(15,"~")
print("'"+tengah3+"'")
tengah3 = tengah3.strip("~")
print("'"+tengah3+"'")
space()

##casefold()= mengembalikan semua karakter dimana semua karakter huruf kecil
txt = "Hello, And Welcome To My World!".casefold()
print(txt)
