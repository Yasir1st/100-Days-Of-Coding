from . import Operasi,Util

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan Tambahkan Data Baru".center(100))
    print("="*100+"\n")

    penulis = input("Penulis \t: ")
    judul = input("Judul \t\t: ")
    while True:
        try:
            tahun = int(input("Tahun \t\t: "))
            if (len(str(tahun)) == 4):
                break
            else:
                print("Tahun Harus Angka Dengan Panjang 4 Karakter, Masukkan Lagi !")
        except:
            print("Tahun Harus Angka Dengan Panjang 4 Karakter, Masukkan Lagi !")

    Operasi.create(tahun,judul,penulis)
    print(" ")
    Util.line()
    print("Ini Adalah Data Baru Anda".center(100))
    read_console()
    

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    Util.line()
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    Util.lineMini()
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    # Footer
    Util.line()
    print(" ")