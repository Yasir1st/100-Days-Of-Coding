import os

def line():
    print("="*50)

if __name__ == "__main__" :
    sistemOperasi = os.name
    
    while True:

        match sistemOperasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

        line()  
        print("SELAMAT DATANG DI PROGRAM".center(50))
        print("DATABASE PERPUSTAKAAN".center(50))
        line()   
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete data")
        line()

        user_option = input("Masukkan Opsi : ")
        line()

        match user_option:
            case "1" : print("Melakukan Read Data")
            case "2" : print("Melakukan Create Data")
            case "3" : print("Melakukan Update Data")
            case "4" : print("Melakukan Delete Data")
        
        line()
        is_continue = input("Lanjut y/n :").upper()
        if is_continue == "N":
            line()
            break

    print("Program Selesai, Terima Kasih :)")
    line()

        