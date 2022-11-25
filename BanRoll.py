# Program Pembelian Banana Roll
import os

line = lambda :print("="*44)

os.system("cls")

# Heading
line()
print("YASIRZ FOOD:)".center(44))
line()
print("Menus".center(44))
line()

print('''Pricing :
- Banana Roll 10k
- Pisang Nugget 8k
- Topping 3k''')

line()
print("Input Data Pembelian".center(44))
line()


# Input
nama = input("Nama Pembeli \t\t: ")
banroll = int(input("Jumlah BanRoll \t\t: "))
pisnug = int(input("Jumlah PisNug \t\t: "))
topping = int(input("Jumlah Topping \t\t: "))
line()

# Process Hitung
hargaBanroll = banroll*10000
hargaPisnug = pisnug*8000
hargaTopping = topping*3000
jumlah = hargaBanroll+hargaPisnug+hargaTopping

# Output
print(f" Nama Pembeli \t\t: {nama}")
print(f" Total Pembelian \t: {jumlah}")
line()
print("Terimakasih Telah Berbelanja".center(44))
line()