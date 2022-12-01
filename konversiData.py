import os

os.system("cls")
line = lambda : print("="*44)

line()
print("Konversi Data".center(44))
line()
print('''Pilihan Unit :
1. Byte
2. Kilobyte
3. Megabyte
4. Gigabyte
5. Terabyte
6. Petabyte''')
line()

byte,kb,mb,gb,tb,pb = 1024,1024,1024,1024,1024,1024

print("Masukkan Pilihan Dalam Bentuk Angka :")
fromData = int(input("Dari \t: "))
toData = int(input("Ke \t: "))
line()

if(fromData == 6):
    if(toData == 6):
        print("Petabyte To Petabyte".center(44))
        line()
        inputFrom = int(input("Petabyte \t: "))
        print(f"Petabyte \t: {inputFrom}")
    elif(toData == 5):
        print("Petabyte To Terabyte".center(44))
        line()
        inputFrom = int(input("Petabyte \t: "))
        print(f"Terabyte \t: {inputFrom*tb}")
    elif(toData == 4):
        print("Petabyte To Gigabyte".center(44))
        line()
        inputFrom = int(input("Petabyte \t: "))
        print(f"Gigabyte \t: {inputFrom*tb*gb}")
    elif(toData == 3):
        print("Petabyte To Megabyte".center(44))
        line()
        inputFrom = int(input("Petabyte \t: "))
        print(f"Megabyte \t: {inputFrom*tb*gb*mb}")
    elif(toData == 2):
        print("Petabyte To Kilobyte".center(44))
        line()
        inputFrom = int(input("Petabyte \t: "))
        print(f"Kilobyte \t: {inputFrom*tb*gb*mb*kb}")
    elif(toData == 1):
        print("Petabyte To Byte".center(44))
        line()
        inputFrom = int(input("Petabyte \t: "))
        print(f"Byte \t\t: {inputFrom*tb*gb*mb*kb*byte}")
    else:
        print("Pilihan Tidak Ada !!")

elif(fromData == 5):
    if(toData == 6):
        print("Terabyte To Petabyte".center(44))
        line()
        inputFrom = int(input("Terabyte \t: "))
        print(f"Petaabyte \t: {inputFrom/pb}")
    elif(toData == 5):
        print("Terabyte To Terabyte".center(44))
        line()
        inputFrom = int(input("Terabyte \t: "))
        print(f"Terabyte \t: {inputFrom}")
    elif(toData == 4):
        print("Terabyte To Gigabyte".center(44))
        line()
        inputFrom = int(input("Terabyte \t: "))
        print(f"Gigabyte \t: {inputFrom*gb}")
    elif(toData == 3):
        print("Terabyte To Megabyte".center(44))
        line()
        inputFrom = int(input("Terabyte \t: "))
        print(f"Megabyte \t: {inputFrom*gb*mb}")
    elif(toData == 2):
        print("Terabyte To Kilobyte".center(44))
        line()
        inputFrom = int(input("Terabyte \t: "))
        print(f"Kilobyte \t: {inputFrom*gb*mb*kb}")
    elif(toData == 1):
        print("Terabyte To Byte".center(44))
        line()
        inputFrom = int(input("Terabyte \t: "))
        print(f"Byte \t\t: {inputFrom*gb*mb*kb*byte}")
    else:
        print("Pilihan Tidak Ada !!")

elif(fromData == 4):
    if(toData == 6):
        print("Gigabyte To Petabyte".center(44))
        line()
        inputFrom = int(input("Gigabyte \t: "))
        print(f"Petabyte \t: {inputFrom/tb/pb}")
    elif(toData == 5):
        print("Gigabyte To Terabyte".center(44))
        line()
        inputFrom = int(input("Gigabyte \t: "))
        print(f"Terabyte \t: {inputFrom/tb}")
    elif(toData == 4):
        print("Gigabyte To Gigabyte".center(44))
        line()
        inputFrom = int(input("Gigabyte \t: "))
        print(f"Gigabyte \t: {inputFrom}")
    elif(toData == 3):
        print("Gigabyte To Megabyte".center(44))
        line()
        inputFrom = int(input("Gigabyte \t: "))
        print(f"Megabyte \t: {inputFrom*mb}")
    elif(toData == 2):
        print("Gigabyte To Kilobyte".center(44))
        line()
        inputFrom = int(input("Gigabyte \t: "))
        print(f"Kilobyte \t: {inputFrom*mb*kb}")
    elif(toData == 1):
        print("Gigabyte To Byte".center(44))
        line()
        inputFrom = int(input("Gigabyte \t: "))
        print(f"Byte \t\t: {inputFrom*mb*kb*byte}")
    else:
        print("Pilihan Tidak Ada !!")

elif(fromData == 3):
    if(toData == 6):
        print("Megabyte To Petabyte".center(44))
        line()
        inputFrom = int(input("Megabyte \t: "))
        print(f"Petabyte \t: {inputFrom/gb/tb/pb}")
    elif(toData == 5):
        print("Megabyte To Terabyte".center(44))
        line()
        inputFrom = int(input("Megabyte \t: "))
        print(f"Terabyte \t: {inputFrom/gb/tb}")
    elif(toData == 4):
        print("Megabyte To Gigabyte".center(44))
        line()
        inputFrom = int(input("Megabyte \t: "))
        print(f"Gigabyte \t: {inputFrom/gb}")
    elif(toData == 3):
        print("Megabyte To Megabyte".center(44))
        line()
        inputFrom = int(input("Megabyte \t: "))
        print(f"Megabyte \t: {inputFrom}")
    elif(toData == 2):
        print("Megabyte To Kilobyte".center(44))
        line()
        inputFrom = int(input("Megabyte \t: "))
        print(f"Kilobyte \t: {inputFrom*kb}")
    elif(toData == 1):
        print("Megabyte To Byte".center(44))
        line()
        inputFrom = int(input("Megabyte \t: "))
        print(f"Byte \t\t: {inputFrom*kb*byte}")
    else:
        print("Pilihan Tidak Ada !!")

elif(fromData == 2):
    if(toData == 6):
        print("Kilobyte To Petabyte".center(44))
        line()
        inputFrom = int(input("Kilobyte \t: "))
        print(f"Petabyte \t: {inputFrom/mb/gb/tb/pb}")
    elif(toData == 5):
        print("Kilobyte To Terabyte".center(44))
        line()
        inputFrom = int(input("Kilobyte \t: "))
        print(f"Terabyte \t: {inputFrom/mb/gb/tb}")
    elif(toData == 4):
        print("Kilobyte To Gigabyte".center(44))
        line()
        inputFrom = int(input("Kilobyte \t: "))
        print(f"Gigabyte \t: {inputFrom/mb/gb}")
    elif(toData == 3):
        print("Kilobyte To Megabyte".center(44))
        line()
        inputFrom = int(input("Kilobyte \t: "))
        print(f"Megabyte \t: {inputFrom/mb}")
    elif(toData == 2):
        print("Kilobyte To Kilobyte".center(44))
        line()
        inputFrom = int(input("Kilobyte \t: "))
        print(f"Kilobyte \t: {inputFrom}")
    elif(toData == 1):
        print("Kilobyte To Byte".center(44))
        line()
        inputFrom = int(input("Kilobyte \t: "))
        print(f"Byte \t\t: {inputFrom*byte}")
    else:
        print("Pilihan Tidak Ada !!")

elif(fromData == 1):
    if(toData == 6):
        print("Byte To Petabyte".center(44))
        line()
        inputFrom = int(input("Byte \t: "))
        print(f"Petabyte \t: {inputFrom/kb/mb/gb/tb/pb}")
    elif(toData == 5):
        print("Byte To Terabyte".center(44))
        line()
        inputFrom = int(input("Byte \t: "))
        print(f"Terabyte \t: {inputFrom/kb/mb/gb/tb}")
    elif(toData == 4):
        print("Byte To Gigabyte".center(44))
        line()
        inputFrom = int(input("Byte \t: "))
        print(f"Gigabyte \t: {inputFrom/kb/mb/gb}")
    elif(toData == 3):
        print("Byte To Megabyte".center(44))
        line()
        inputFrom = int(input("Byte \t: "))
        print(f"Megabyte \t: {inputFrom/kb/mb}")
    elif(toData == 2):
        print("Byte To Kilobyte".center(44))
        line()
        inputFrom = int(input("Byte \t: "))
        print(f"Kilobyte \t: {inputFrom/kb}")
    elif(toData == 1):
        print("Byte To Byte".center(44))
        line()
        inputFrom = int(input("Byte \t: "))
        print(f"Byte \t\t: {inputFrom}")
    else:
        print("Pilihan Tidak Ada !!")

else:
    print("Pilihan Tidak Ada !!")

line()