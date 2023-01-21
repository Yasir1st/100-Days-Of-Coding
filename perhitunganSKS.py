sks = int(input("Jumlah kredit(SKS) perkuliahan yang sudah diambil : "))

if(sks > 128): print("Mahasiswa tahun ke empat")
elif(sks >= 85 and sks <=128):print("Mahasiswa tahun ke tiga")
elif(sks >= 49 and sks <=84):print("Mahasiswa tahun ke dua")
elif(sks <= 48):print("Mahasiswa tahun ke pertama")
