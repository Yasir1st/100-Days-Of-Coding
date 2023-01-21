nilai = 73

if nilai >= 0 and nilai <= 100 :
    if nilai >= 86 and nilai <= 100 :grade = "A"
    elif nilai >= 53 and nilai <= 86 :grade = "B"
    elif nilai == 51 or nilai == 52 :grade = "C"
    elif nilai < 51 : grade = "D"

print("Grade Nilai = ",grade)

if not (nilai >= 0 and nilai <= 100 ): #dapat diganti dengan pernyataan else
    print("Nilai yang anda masukkan salah") 