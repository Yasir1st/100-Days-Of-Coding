def line():
    print("="*40)

# operator dictionary
line()
print("Dictionary Operation".center(40))
line()
dict_Esport = {
	"btr":"Bigetron Win",
    "evos":"Evos Roar",
    "rrq":"Viva Rex Regum Qeon"
}
print(dict_Esport)

# panjang dictionary
line()
LENDICT = len(dict_Esport) #variabel yang menampung method pada dict harus menggunakan Huruf Kapital semua
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
line()
KEY = "btr"
CHECKKEY = KEY in dict_Esport #variabel yang menampung method pada dict harus menggunakan Huruf Kapital semua
print(f"apakah {KEY} ada di dict_Esport: {CHECKKEY}")

# mengakses value (read) dengan get
line()
print(dict_Esport["btr"])
print(dict_Esport.get("onic")) #jika key yang di panggil menggunakan get tidak terdapat pada dictinary maka akan menampilkan messege None
print(dict_Esport.get("Onic","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
line()
#   mengapdate data tanpa method
dict_Esport["rrq"] = "Viva RRQ"
print(dict_Esport)
#   menambahkan data tanpa method
dict_Esport["onic"] = "Sonic Onic"
print(dict_Esport)

# Meng update data dan menambahkan data menggunakan method update()
line()
dict_Esport.update({"btr":"BTR Win"}) # jika key didalam method update() ada pada dictionary maka akan meng update data tersebut
print(dict_Esport)
dict_Esport.update({"ae":"Alter Ego Go Go Go"}) # jika key dalam method update() tdk terdapat pada dictionary maka akan menambahkan data tersebut ke dictionary
print(dict_Esport)

# mendelete data pada dictionary
line()
del dict_Esport["ae"]
print(dict_Esport)
line()