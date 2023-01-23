import os
os.system("cls")

def line():
    print("="*45)

point = 0

line()
print("Program Test Kepribadian".center(45))
line()

# Pertanyaan Pertama 
print("Pertanyaan 1".center(45))
line()

print("1. Kamu menginginkan orang yang seperti apa untuk menjadi pasanganmu?")
print('''
    A. Kaya
    B. Seksi
    C. Teman dekat
    D. Memiliki sifat yang sama
    E. Yang aku cinta
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 1
        break
    elif(jawab == "B"):
        point += 4
        break
    elif(jawab == "C"):
        point += 3
        break
    elif(jawab == "D"):
        point += 4
        break
    elif(jawab == "E"):
        point += 5
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Kedua 
print("Pertanyaan 2".center(45))
line()

print("2. Di rumahmu, ruangan mana yang menjadi tempat favoritmu?")
print('''
    A. Dapur
    B. Kamar tidur
    C. Garasi
    D. Teras/ Ruang tamu
    E. Lainnya
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 1
        break
    elif(jawab == "B"):
        point += 3
        break
    elif(jawab == "C"):
        point += 4
        break
    elif(jawab == "D"):
        point += 5
        break
    elif(jawab == "E"):
        point += 2
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ketiga 
print("Pertanyaan 3".center(45))
line()

print("3. Dalam 15 tahun ke depan, apa yang ingin kamu lakukan?")
print('''
    A. Berkeluarga
    B. Jadi CEO
    C. Keliling dunia
    D. Tetap menjomblo
    E. Jadi selebriti
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 2
        break
    elif(jawab == "B"):
        point += 1
        break
    elif(jawab == "C"):
        point += 4
        break
    elif(jawab == "D"):
        point += 3
        break
    elif(jawab == "E"):
        point += 5
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ke-empat
print("Pertanyaan 4".center(45))
line()

print("4. Apa yang ingin kamu lakukan untuk bersenang-senang?")
print('''
    A. Nongkrong
    B. Makan di kafe
    C. Nonton film
    D. Shopping
    E. Jalan-jalan sama pacar
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 4
        break
    elif(jawab == "B"):
        point += 1
        break
    elif(jawab == "C"):
        point += 3
        break
    elif(jawab == "D"):
        point += 5
        break
    elif(jawab == "E"):
        point += 2
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ke-lima
print("Pertanyaan 5".center(45))
line()

print("5. Pilih binatang yang kamu suka?")
print('''
    A. Harimau/ Beruang
    B. Singa/ Merak
    C. Katak/ Babi
    D. Ular/ Kadal
    E. Gajah/ Kucing
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 4
        break
    elif(jawab == "B"):
        point += 1
        break
    elif(jawab == "C"):
        point += 3
        break
    elif(jawab == "D"):
        point += 5
        break
    elif(jawab == "E"):
        point += 2
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ke-enam 
print("Pertanyaan 6".center(45))
line()

print("6. Apa warna favorit kamu?")
print('''
    A. Merah/ Pink
    B. Kuning/ Orange
    C. Hijau/ Coklat
    D. Ungu/ Biru
    E. Putih/ Hitam/ Lainnya
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 4
        break
    elif(jawab == "B"):
        point += 3
        break
    elif(jawab == "C"):
        point += 2
        break
    elif(jawab == "D"):
        point += 1
        break
    elif(jawab == "E"):
        point += 5
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ke-tujuh
print("Pertanyaan 7".center(45))
line()

print("7. Apa yang biasanya kamu lakukan saat santai?")
print('''
    A. Ngegosip
    B. Tidur
    C. Goda teman
    D. Memasak
    E. Tetap kerja
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 4
        break
    elif(jawab == "B"):
        point += 3
        break
    elif(jawab == "C"):
        point += 5
        break
    elif(jawab == "D"):
        point += 1
        break
    elif(jawab == "E"):
        point += 2
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ke-delapan
print("Pertanyaan 8".center(45))
line()

print("8. Apa minuman favorit kamu?")
print('''
    A. Teh/ Kopi
    B. Lemon/ Jus buah
    C. Air putih
    D. Minuman keras
    E. Soft drink
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 3
        break
    elif(jawab == "B"):
        point += 2
        break
    elif(jawab == "C"):
        point += 5
        break
    elif(jawab == "D"):
        point += 4
        break
    elif(jawab == "E"):
        point += 1
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ke-sembilan
print("Pertanyaan 9".center(45))
line()

print("9. Menurutmu, apa yang terbaik dari dirimu?")
print('''
    A. Kuat
    B. Pintar
    C. Cantik/ Tampan
    D. Baik hati
    E. Setia
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 4
        break
    elif(jawab == "B"):
        point += 2
        break
    elif(jawab == "C"):
        point += 5
        break
    elif(jawab == "D"):
        point += 3
        break
    elif(jawab == "E"):
        point += 1
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Pertanyaan Ke-sepuluh
print("Pertanyaan 10".center(45))
line()

print("10. Apa kekurangan dirimu?")
print('''
    A. Penakut
    B. Wajah pas-pasan
    C. Tidak pintar
    D. Lemah
    E. Tidak ada
''')

while True:
    jawab = input("Jawab : ").upper()
    if(jawab == "A"):
        point += 5
        break
    elif(jawab == "B"):
        point += 4
        break
    elif(jawab == "C"):
        point += 1
        break
    elif(jawab == "D"):
        point += 3
        break
    elif(jawab == "E"):
        point += 2
        break
    else:
        print("Jawaban Tidak Ditemukan, Coba Lagi")
line()

# Hasil Kepribadian
print("Kepribadian Kamu")
line()

if(point >= 10 and point <= 15):
    print(" Kamu adalah seorang pencinta kuliner. Kamu suka makan dan memiliki nafsu makan yang besar.")
    print(" Bahkan kamu akan makan dan terus makan. Tidak mengenal kata 'kenyang', tapi kamu akan berhenti kalau sudah puas.")
    print(" Hal tersebut pun membuatmu memiliki kepribadian sangat boros. Selain itu, saat perutmu kekenyangan, juga akan membuatmu malas bergerak.")
    print(" Maka dari itu, cobalah untuk mengendalikan nafsu makan, dengan cara makan secukupnya, dan berusahalah berhenti saat perut terasa kenyang.")
elif(point >= 16 and point <= 21):
    print(" Kamu memiliki kepribadian sangat kompetitif dan menginginkan semua kemewahan yang ada dalam kehidupan ini.")
    print(" Semakin banyak yang kamu miliki, semakin banyak juga keinginan yang ingin didapatkan.")
    print(" Bahkan tidak ada yang bisa memuaskan dan menghentikan sifat buruk yaitu keserakahan yang ada dalam dirimu.")
    print(" Tapi ingatlah, yang bisa menghentikan sifat buruk yaitu keserakahanmu adalah waktu, dan 'waktu' tidak bisa di beli oleh kemewahan yang kamu kumpulkan.")
elif(point >= 22 and point <= 26):
    print(" Kamu memiliki kepribadian sangat ambisius dan memiliki impian yang besar untuk masa depanmu.")
    print(" Namun kamu tidak memiliki kemampuan yang cukup untuk mewujudkannya.")
    print(" Terkadang dari sifat buruk yaitu iri hati yang ada dalam dirimu, bisa menimbulkan rasa cemburu pada 'kepunyaan' orang lain.")
    print(" Entah itu, pencapaian dalam mendapatkan kekayaan, jabatan atau pangkat, serta prestasi.")
    print(" Bahkan sifat buruk iri hatimu itu dapat menyebabkan kemalangan, dan kamu harus tahu kalau sifat buruk iri hati adalah salah satu penyebab utama ketidakbahagiaan diri sendiri.")
    print(" Maka dari itu, cobalah untuk menghilangkan sifat buruk dengan cara mensyukuri nikmat yang sudah kamu miliki, karena orang lain belum tentu mendapatkannya.")
elif(point >= 27 and point <= 32):
    print(" Kamu memiliki kepribadian sangat cerdas dan berbakat. Hal itulah yang membuatmu selalu berbangga diri.")
    print(" Kamu sering merasa lebih baik dan lebih pintar dari orang lain. Sehingga muncullah sifat buruk yang ada dalam dirimu, yaitu sombong.")
    print(" Sifat buruk itu juga bisa membuatmu tidak disukai dan malah dijauhi teman atau rekan.")
    print(" Ingatlah, tidak selamanya kamu bisa mengatasi segala hal sendirian. Sebab suatu hari nanti, kamu pasti akan membutuhkan bantuan orang lain.")
    print(" Jadi cobalah untuk lebih rendah hati, agar hidupmu lebih berwarna.")
elif(point >= 33 and point <= 39):
    print(" Kamu adalah seorang pemimpi. Kamu memiliki banyak rencana dan tujuan besar.")
    print(" Sayangnya, sifat buruk yang ada dalam dirimu yang justru lebih menonjol, yaitu rasa malas. Kamu terlalu malas untuk melakukan apa pun dalam mencapai impianmu.")
    print(" Sebenarnya kamu memiliki banyak potensi diri, tetapi kamu cenderung melakukan pekerjaan sesedikit mungkin dan suka menunda-nunda pekerjaan.")
    print(" Jika kamu menginginkan kesuksesan, maka segeralah buang sifat buruk yang ada dalam dirimu, karena kemalasanmu hanya akan menjadi penghalang tercapainya impian.")
elif(point >= 40 and point <= 44):
    print(" Kamu memiliki kepribadian sangat bersemangat dan banyak ide. Tetapi sifat buruk yang ada dalam dirimu yaitu gampang marah, seringkali muncul.")
    print(" Kemarahanmu akan muncul ketika ide yang kamu buat tidak sesuai dengan apa yang kamu harapkan.")
    print(" Selain mempunyai sifat buruk yaitu gampang marah, kamu juga cenderung memiliki rasa balas dendam kepada orang yang kamu anggap bertanggung jawab atas ketidaktercapainya harapanmu.")
    print(" Bahkan kamu juga memiliki sifat buruk yaitu gampang merusak diri yang bisa berbahaya, baik untuk dirimu sendiri maupun orang di sekitar.")
    print(" Maka dari itu, cobalah untuk tarik nafas panjang saat kamu merasa akan marah. Sebab cara tersebut bisa meredam amarahmu.")
elif(point >= 45 and point <= 50):
    print(" Kamu adalah seorang yang bernampilan modis atau menarik yang menghargai keindahan.")
    print(" Namun terkadang kamu suka menyalahgunakan kecantikan atau ketampananmu, demi menggaet seseorang.")
    print(" Jika kamu menginginkan sesuatu, kamu harus mendapatkannya walaupun menggunakan segala cara yang diperlukan, dan biasanya kamu akan mengeluarkan sifat buruk yang ada dalam dirimu yaitu hawa nafsu diselimuti gairah menggebu.")
    print(" Mungkin solusi terbaik untukmu saat ini adalah cobalah mengalihkan topik yang membuatmu bergairah.")
    print(" Selain itu, kamu juga bisa menggunakan energimu untuk hal lain yang lebih bermanfaat. Salah satu cara yang paling efektif dengan cara berolahraga.")

line()
print("Terima Kasih".center(45))
line()