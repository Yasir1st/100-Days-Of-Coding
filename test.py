def line():
    print("="*44)
    return

def title(judul):
    line()
    print(judul.center(44))
    line()

title("Test 1")
angka = int(input("Masukkan Angka Akhir :"))

if(angka % 2 == 0):
    for i in range(2,angka+1,2):
        print(i,end=" ")
    print()
elif(angka % 2 != 0):
    for i in range(1,angka+1,2):
        print(i,end=" ")
    print()

title("Test 2")
angka = int(input("Masukkan Angka Akhir :"))

if(angka >= 5 and angka <= 50):
    if(angka % 2 == 0):
        for i in range(2,angka+1,2):
            print(i,end=" ")
    elif(angka % 2 != 0):
        for i in range(1,angka+1,2):
            print(i,end=" ")
    print()
else:
    print("out of range")

title("Test 3")
angka = int(input("Masukkan Angka :"))

for i in range(1,angka+1):
    print("*"*i)

title("Test 4")
angka = int(input("Masukkan Angka :"))

for i in range(1,angka+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
line()

# Test From Pak Alam :)