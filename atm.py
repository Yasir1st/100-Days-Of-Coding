import os

def line():
    '''line'''
    print("="*50)
    return

os.system("cls")

line()
print("ATM BRI".center(50))
line()
print('''Menu :
1. Penarikan
2. Penyetoran
3. Cek Saldo''')

saldo = 0

while True:
    line()
    menu = int(input("Pilih Menu \t: "))
    line()

    if(menu == 1):
        tarik_saldo = int(input("Masukkan Nominal Penarikan \t: Rp."))
        if(saldo > tarik_saldo):
            saldo -= tarik_saldo
            print(f"Sisa Saldo \t\t\t: Rp.{saldo}")
        else:
            print("Saldo Anda Kurang")
    elif(menu == 2):
        tambah_saldo = int(input("Masukkan Nominal Penyetoran \t: Rp."))
        saldo += tambah_saldo
        print(f"Sisa Saldo \t\t\t: Rp.{saldo}")
    elif(menu == 3):
        print(f"Saldo \t\t\t\t: Rp.{saldo}")
    line()

    lanjut = input("Lanjut Bro(y/n) ? ")
    if(lanjut == "n"):
        line()
        print("Terima Kasih Telah Berkunjung Di BRI".center(50))
        break
line()