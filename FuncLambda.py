# Lambda function
line = lambda : print("="*50)

line()
print("Lambda Function".center(50))
line()

# cara biasa function kuadrat
def f_kuadrat(angka):
    '''Kuadrat'''
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# kita coba dengan lambda
# output = lambda argument: expression <= Bentuk umum lambda function
kuadrat = lambda angka : angka**2
print(f"hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")
line()

## contoh kegunaan lambda function

# sorting untuk list biasa
data_list = ["Yasir","Kazuha","Kim Ran"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting dia pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

# sort pakai lambda
data_list = ["Yasir","Kazuha","Kim Ran"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")
line() 

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_3)
line() 

# anonymous function
# currying <- Haskell Curry 

def pangkat_biasa(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat_biasa(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkatt(n):
    return lambda angka:angka**n

pangkat2 = pangkatt(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat3 = pangkatt(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkatt(4)(5)}")
line()