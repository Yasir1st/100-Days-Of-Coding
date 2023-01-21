import os
os.system("cls")

def line():
    print("="*50)

pin = "913451"

data_user = {
    'user1':'yasir',
    'user2':'ken'
    }

data_briva = {
    'no_briva1':'123456789',
    'no_briva2':'987654321'
}

data_ukt = {
     'ukt_user1':1500000,
     'ukt_user2':1000000
}

line()
print("Program Pembayaran UKT BRIVA".center(50))

while True:
    line()
    pin_atm = input("Masukkan PIN anda : ")

    if(pin_atm == pin):
        while True:
            input_no_briva = input("Masukkan No Briva Anda : ")

            if(input_no_briva == data_briva['no_briva1']):
                line()
                print(f"Nama \t\t: {data_user['user1']}")
                print(f"No Briva \t: {data_briva['no_briva1']}")
                UKT = data_ukt['ukt_user1']
                print(f"UKT \t\t: {UKT}")


                cek = input("Apakah Sudah Benar Atau Tidak(y/n) ? ")
                if cek == "y":
                    line()
                    break

            elif(input_no_briva == data_briva['no_briva2']):
                line()
                print(f"Nama \t\t: {data_user['user2']}")
                print(f"No Briva \t: {data_briva['no_briva2']}")
                UKT = data_ukt['ukt_user2']
                print(f"UKT \t\t: {UKT}")


                cek = input("Apakah Sudah Benar Atau Tidak(y/n) ? ")
                if cek == "y":
                    line()
                    break
            else:
                print("Anda Belum Terdaftar, Coba Lagi")
        break
    else:
        print("PIN anda Salah silahkan coba lagi")

while True:
    input_pembayaran = int(input("Masukkan Jumlah Uang Pembayaran UKT : Rp."))
    if(input_pembayaran == UKT):
        line()
        print("Pembayaran Berhasil")
        break
    elif(input_pembayaran > UKT):
        line()
        print("Pembayaran Berhasil,")
        print(f"Kembalian Anda RP.{input_pembayaran-UKT}")
        break
    else:
        line()
        print("Uang Anda Kurang, Masukkan Lagi")

line()