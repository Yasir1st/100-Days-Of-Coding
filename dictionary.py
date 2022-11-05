def line():
    print("-"*40)
    
line()

# List / dapat di akses menggunakan index
list_manga = ["Haikyuu!","Solo Leveling","Domestik Na Kanojo"]
print(list_manga[0])
line()

# Tuples / datanya tidak dapat di rubah namun dapat di akses menggunakan index
tuple_drakor = ("Big Mouth","Business Proposal","18 Again")
print(tuple_drakor[1])
line()
# tuple_drakor.append(1) / jika ingin mengubah data pada tuples maka akan terjadi error

# Sets / tidak dapat di akses menggunakan index / namum dapat masih dapat menggunakan method
sets_ganjil = {1,3,5,7,9}
# print(sets_ganjil[1]) / maka akan error
banyaknya_data = len(sets_ganjil)
print(banyaknya_data)
line()

# Dictionari(Dict) -> associative array
# Datanya dapat di akses mengginakan -> key
dict_kpop = {
    # Key | Value
    "bp" :"BlackPink",
    "ae" :"Aespa",
    "tw" :"Twice",

    # Menggunakan Number pada valuenya juga bisa
    "cr" :7,

    # Bahkan membuat list didalam dict jga bisa
    "lb" :["Jisoo","Karina","Nancy","Tzuyu"]

    # Selain di atas , kita jga dapat menambahkan dict di dalam dict  
}

print(dict_kpop)
line()
print(dict_kpop["ae"])
line()
print(dict_kpop["cr"])
line()
print(dict_kpop["lb"])
line()

# Kamu Nanyaaaa , rawrrr :)