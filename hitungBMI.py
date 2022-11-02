def line():
    print("-"*50)
    
#Hitung BMI
line()
print("Program Menghitung BMI(Body Mass Index)")
line()

def hitung_bmi(berat,tinggi):
    bmi = berat/(tinggi*tinggi)
    line()
    print(f"Body Mass Index : {bmi:.2f}")
    line()

    if(bmi < 17):
        print("Kategori : Sangat Kurus")
    elif(bmi >= 17 and bmi < 18.5):
        print("Kategori : Kurus")
    elif(bmi >= 18.5 and bmi <= 25):
        print("Kategori : Normal")
    elif(bmi > 25 and bmi <= 27):
        print("Kategori : Gemuk")
    elif(bmi > 27):
        print("Kategori :Sangat Gemuk")
    line()

berat_badan = int(input("Masukkan Berat Badan(KG) : "))
tinggi_badan = float(input("Masukkan Tinggi Badan(M) : "))
hitung_bmi(berat_badan,tinggi_badan)