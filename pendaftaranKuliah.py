import os
os.system("cls")

def line():
    print("="*50)

line()
print("Program Pendaftaran Kuliah".center(50))
line()

nama = input("Nama \t\t\t: ")
usia = int(input("Usia \t\t\t: "))
nilai_rata_rata = int(input("Nilai Rata - Rata Ujian\t: ")) 
point = 0
line()
if usia >= 19:
    if(nilai_rata_rata >= 81):
        # soal no 1
        print("1. Gunung tertinggi di dunia adalah ? ")
        print("   A. Everest")
        print("   B. Jaya Wijaya")
        print("   C. Klimanjaro")
        print("   D. Elbrus")
        
        no_1 = input("\n   Jawab : ").upper()

        if(no_1 == "A"):
            point += 1 
        else:
            point += 0 

        # soal no 2
        print("\n2. Negara terkecil didunia ? ")
        print("   A. Filiphina")
        print("   B. Guam")
        print("   C. Vatikan")
        print("   D. Timor Leste")
        
        no_2 = input("\n   Jawab : ").upper()

        if(no_2 == "C"):
            point += 1 
        else:
            point += 0 

        # soal no 3
        print("\n3. Genre game genshin impact ? ")
        print("   A. MMORPG")
        print("   B. RPG")
        print("   C. Battleroyale")
        print("   D. Music Game")
        
        no_3 = input("\n   Jawab : ").upper()

        if(no_3 == "B"):
            point += 1 
        else:
            point += 0
        line()
        
        print(f"Jawaban Benar = {point}")
        if point >= 2:
            print("Kamu Diterima, Selamat Menikmati Kuliah")
        else:
            print("Kamu Tidak Diterima, Coba Lagi Tahun Depan")
    else:
        print("Nilai Anda Tidak Memenuhi")
else:
    print("Anda Masih Terlalu Muda Silahkan Coba Lagi Tahun depan")

line()