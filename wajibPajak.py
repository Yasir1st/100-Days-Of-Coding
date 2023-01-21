import os

line = lambda :print("="*40)

os.system("cls")
line()
print("Wajib Pajak".center(40))
line()
 
# input
gaji = int(input("Jumlah Gaji \t: "))
pekerjaan = input("Pekerjaan \t: ")
line()

def show(jumlah_pajak):
    print(f"Pajak \t\t: Rp.{jumlah_pajak:.2f}")
    print(f"Gaji Bersih \t: Rp.{(gaji-jumlah_pajak):.2f}")

# Kondisi
if(gaji >= 20000000 and pekerjaan == "PNS"):
    pajak = gaji*8/100
    show(pajak)
elif(gaji >= 10000000 and pekerjaan == "PNS"):
    pajak = gaji*5/100
    show(pajak)
elif(gaji >= 20000000):
    pajak = gaji*5/100
    show(pajak)
elif(gaji >= 10000000):
    pajak = gaji*2/100
    show(pajak)
elif(pekerjaan == "PNS"):
    pajak = gaji*3/100
    show(pajak)
else:
    pajak = 0
    show(pajak)
line()
