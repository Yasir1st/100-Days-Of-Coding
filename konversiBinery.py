import os

os.system("cls")
line = lambda : print("="*44)

line()
print("Konversi Biner And Octet".center(44))
line()
pilihan1 = input("Konversi \t: ").lower()
pilihan2 = input("To \t\t: ").lower()

if(pilihan1 == "octet" and pilihan2 == "biner"):
    line()
    print("Octet To Biner".center(44))
    while True:
        line()
        octet = int(input("Masukkan Angka Octet \t: "))

        satu = octet % 2
        bagi_satu = octet // 2

        dua = bagi_satu % 2
        bagi_dua = bagi_satu // 2

        tiga = bagi_dua % 2
        bagi_tiga = bagi_dua // 2

        empat = bagi_tiga % 2
        bagi_empat = bagi_tiga // 2

        lima = bagi_empat % 2
        bagi_lima = bagi_empat // 2

        enam = bagi_lima % 2
        bagi_enam = bagi_lima // 2

        tujuh = bagi_enam % 2
        bagi_tujuh = bagi_enam // 2

        delapan = bagi_tujuh % 2

        print("Biner \t\t\t:",delapan,tujuh,enam,lima,empat,tiga,dua,satu)
        line()
        isContinue = input("Lanjut gak(y/n) ? ")
        if isContinue == "n":
            line()
            break

elif(pilihan1 == "biner" and pilihan2 == "octet"):
    line()
    print("Biner To Octet".center(44))
    while True:
        line()
        biner1 = int(input("Biner ke-1 \t: "))
        biner2 = int(input("Biner ke-2 \t: "))
        biner3 = int(input("Biner ke-3 \t: "))
        biner4 = int(input("Biner ke-4 \t: "))
        biner5 = int(input("Biner ke-5 \t: "))
        biner6 = int(input("Biner ke-6 \t: "))
        biner7 = int(input("Biner ke-7 \t: "))
        biner8 = int(input("Biner ke-8 \t: "))
        line()
        print(f"Biner \t\t: {biner1} {biner2} {biner3} {biner4} {biner5} {biner6} {biner7} {biner8}")
        print(f"Octet \t\t: {(biner1*128)+(biner2*64)+(biner3*32)+(biner4*16)+(biner5*8)+(biner6*4)+(biner7*2)+(biner8*1)}")
        line()

        isContinue = input("Lanjut gak(y/n) ? ")
        if isContinue == "n":
            line()
            break

else:
    print("Anda Salah Input Bro :( ")
    line()