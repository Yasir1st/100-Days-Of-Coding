def line():
    print("="*44)

line()
print("Copy and Pop Dictionary".center(44))
line()
dict_univ = {
    "UNSULBAR":"Universitas Sulawesi Barat",
    "UNSRI":"Universi Sriwijaya",
    "UNHAS":"Universitas Hasanuddin",
    "UI":"Universitas Indonesia",
    "UNPAD":"Universitas Padjajaran"
}

university = dict_univ # jdi dapat disimpulkan bahwa jika hanya menggunakan seperti ini tdk dapat mengcopy secara keseluruhan


print(f"Dictionary Universitas : {dict_univ}")
line()
print(f"University : {university}")
line()
line()
# Mengupdate nilai dalam sebuah dictionary (semua data terupdate jika hanya menggunakan cara di atas)
dict_univ["UNSRI"] = "UNIVERSITAS SRIWIJAYA"
print(f"Dictionary Universitas : {dict_univ}")
line()
print(f"University : {university}")
line()
print("Copy()".center(44))
line()

# Mengcopy Dictionary(cara ini dapat mengcopy secara keseluruhan isi dictionary)
dict_university = dict_univ.copy()
print(f"Dictionary Universitas : {dict_univ}")
line()
print(f"Dictionary University : {dict_university}")
line()
print("Mengupdate Salah Satu Value Dictionary".center(44))
line()

# Jika kita mengapdate salah 1 value dari dictionary yang telah di copy , dictionary sebelumnya tdk berubah(copy())
dict_university["UNSULBAR"] = "UNIVERSITAS SULAWESI BARAT"
print(f"Dictionary Universitas : {dict_univ}")
line()
print(f"Dictionary University : {dict_university}")
line()

# pop() dictionary
print("pop()".center(44))
line()
unsulbar = dict_university.pop("UNSULBAR") # Dengan Cara ini kita mentransfer data unsulbar ke variabel unsulbar
print(f"Unsulbar : {unsulbar}")
line()
print(f"Dictionary University : {dict_university}") # Data unsulbar tdk tampil lagi di dictionary karena telah di transfer
line()

# popitem() dictionary
print("popitem()".center(44))
line()
last_univ = dict_university.popitem() # Mentransfer data terakhir ke variabel last_univ(key dan value) dalam bantuk Tuples
print(f"Last Univ : {last_univ}")
line()
print(f"Dictionary University : {dict_university}") # Data terakhir tdk tampil lagi di dictionary karena telah di transfer
line()

