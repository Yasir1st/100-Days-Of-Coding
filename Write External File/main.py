# 1. mode write

# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya

with open("Write External File/data_1.txt",'w',encoding="utf-8") as file:
    file.write("Van Dijk")

with open("Write External File/data_1.txt",'w',encoding="utf-8") as file:
    file.write("Varane")

with open("Write External File/data_1.txt",'w',encoding="utf-8") as file:
    file.write("Rudiger")

# 2. mode append / bisa menambahkan data, namun filenya harus dibuat terlebih dahulu menggunakan mode w atau manual

with open("Write External File/data_2.txt",'w',encoding="utf-8") as file:
    file.write("Neymar\n")

with open("Write External File/data_2.txt",'a',encoding="utf-8") as file:
    file.write("Messi\n")

with open("Write External File/data_2.txt",'a',encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")

# 3. mode r+ / bisa menimpa data dan bisa juga read data didalamnya

with open("Write External File/data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("Write External File/data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("Write External File/data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("Write External File/data_3.txt",'r+',encoding="utf-8") as file:
    file.write("Ricarlison") # menimpa isi text sesuai dengan panjang data