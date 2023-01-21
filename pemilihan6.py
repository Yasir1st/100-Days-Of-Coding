nilai = 10

if nilai > 7: #peryataan if disertai kondisi
    print("Cetakini jika kondisi benar") #blok perintah if
elif nilai % 2 == 0: #pernyataan elif disertai kondisi
    print("Cetak ini jika kondisi ELIF dijalankan")#blok perintah elif
else:
    print("Cetak ini jika kondisi salah")#blok perintah else
                                         #dijalankan saat kondisi if elif
                                         #tidak dijalankan

print(nilai) #tidaK termasuk blok perintah if,
             #akan dijalankan saat kondisi benar maupun salah