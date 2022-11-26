# Program Pembelian Banana Roll
import os

line = lambda :print("="*44)

os.system("cls")

line()
print("LaBOBA'S:)".center(44))
line()
print("Menu".center(44))
line()

print('''Drinks
- Vanilla Latte  10k
- Matcha         10k
- Brown Sugar    10k
- Coklat Nut     12k

Topping
- Chesee Cloud   5k
- Oreo           3k
- Boba           1k
- Ice Cream      4k

Extra Ice        1k
Extrta Sugar     1k''')
line()

print("Input Pembelian".center(44))
line()

# Minuman 
minuman = input("Varian Minuman \t\t: ").lower()

if(minuman == "vanilla latte" or minuman == "matcha" or minuman == "brown sugar"):
    harga_minuman = 10000
elif(minuman == "coklat nut"):
    harga_minuman = 12000
else:
    print("Variant Tidak Tersedia")
    harga_minuman = 0

# Topping 
topping = input("Topping \t\t: ").lower()

if(topping == "chesee cloud"):
    harga_topping = 5000
elif(topping == "oreo"):
    harga_topping = 3000
elif(topping == "boba"):
    harga_topping = 1000
elif(topping == "ice cream"):
    harga_topping = 4000
else:
    print("Topping Tidak Tersedia")
    harga_topping = 0 

# Ice and Sugar
ice = input("Ice(Less/Normal/Extra) \t: ").lower()
if(ice == "less" or ice == "normal"):
    harga_ice = 0
elif(ice == "extra"):
    harga_ice = 1000
else:
    print("Opsi Tidak Tersedia")
    harga_ice = 0 

sugar = input("Gula(Less/Normal/Extra) : ").lower()
if(sugar == "less" or sugar == "normal"):
    harga_sugar = 0
elif(sugar == "extra"):
    harga_sugar = 1000
else:
    print("Opsi Tidak Tersedia")
    harga_sugar = 0 

line()
print("Detail Pembayaran".center(44))
line()

# Output
print(f"Harga Minuman \t\t: Rp.{harga_minuman}")
print(f"Harga Topping \t\t: Rp.{harga_topping}")
print(f"Ice \t\t\t: Rp.{harga_ice}")
print(f"Sugar \t\t\t: Rp.{harga_sugar}")
print(f"Total Belanja \t\t: Rp.{harga_minuman+harga_sugar+harga_ice+harga_topping}")
line()

print("Kamsahammida!!".center(44))
line()