# Looping Dictionary
def line():
    print("="*37)

line()
print("Dictionary Looping".center(37))
line()
brand_sepatu = {
    "nk":"Nike",
    "vn":"Ventela",
    "as":"Aero Street",
    "cv":"Converse",
    "nb":"New Balance"
}
print(brand_sepatu)
line()
#cara pertama (cara tersebut hanya dapat mengambil key dari dictionary)
for sepatu in brand_sepatu:
    print(sepatu)
line()

# Memanggil key menggunakan method keys()
keys = brand_sepatu.keys()
print(keys)
line()

# Memanggil value / iterables menggunakan get()
for key in brand_sepatu.keys():
    print(brand_sepatu.get(key))
line()

# Memanggil values menggunakan method values()
values = brand_sepatu.values()
print(values)
line()

for value in brand_sepatu.values():
    print(value)
line()

# Menggunakan method items()
items = brand_sepatu.items()
print(items)
line()

for item in brand_sepatu.items():
    print(item) # Outputnya akan berupa Tuples
line()

# Memanggil key dan value menggunakan items()
for key,value in brand_sepatu.items():
    print(f"key = {key}, value = {value}")
line()