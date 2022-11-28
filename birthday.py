import os
import datetime as dt

os.system("cls")

def line():
    '''line'''
    print("="*46)

def line2():
    '''line'''
    print("-"*46)


def title(judul):
    '''title'''
    print(judul.center(46))

# Header
line()
title("Birthday Program")
line()
title("Birdthday Date  :) ")
line()

# Input
TANGGAL = int(input("Tanggal : "))
BULAN = int(input("Bulan \t: "))
TAHUN = int(input("Tahun \t: "))
line()
title("Today Date  :) ")
line()
T_TANGGAL = int(input("Tanggal : "))
T_BULAN = int(input("Bulan \t: "))
T_TAHUN = int(input("Tahun \t: "))
line()

today = dt.date(T_TAHUN,T_BULAN,T_TANGGAL)
birthday = dt.date(TAHUN,BULAN,TANGGAL)

# Ulang Tahun Berikutnya
if(T_BULAN == BULAN):
    if(T_TANGGAL <= TANGGAL):
        next_birthday = dt.date(T_TAHUN,BULAN,TANGGAL)
    else:
        next_birthday = dt.date(T_TAHUN+1,BULAN,TANGGAL)
elif(T_BULAN < BULAN):
    next_birthday = dt.date(T_TAHUN,BULAN,TANGGAL)
else:
    next_birthday = dt.date(T_TAHUN+1,BULAN,TANGGAL)

to_birthday = next_birthday-today
to_bulan = (to_birthday.days % 365)//30
to_hari = (to_birthday.days % 365)%30
to_M_D = str(to_bulan)+" Bulan | "+str(to_hari)+" Hari"

# Details
umur_hari = today-birthday
umur_jam = umur_hari.days*24
umur_menit = (umur_hari.days*24)*60
umur_minggu = umur_hari.days // 7
umur_bulan = umur_hari.days // 30
umur_tahun = umur_hari.days // 365

sisa_bulan = (umur_hari.days % 365)//30
sisa_hari = (umur_hari.days % 365)%30

umur_tahun_ket = str(umur_tahun)+" Tahun"
umur_M_D_ket = str(sisa_bulan)+" Bulan | "+str(sisa_hari)+" Hari"

print(f"|{'USIA':^20}| {'NEXT BIRTHDAY':<22}|")
line2()
print(f"|{umur_tahun_ket:^20}| {next_birthday:%A} ,{next_birthday}    |")
print(f"|{umur_M_D_ket:^20}| {to_M_D:<22}|")
line()
title("Ringkasan")
line2()
print(f"|{'TAHUN':^14}|{'BULAN':^14}|{'MINGGU':^14}|")
print(f"|{umur_tahun:^14}|{umur_bulan:^14}|{umur_minggu:^14}|")
line2()
print(f"|{'HARI':^14}|{'JAM':^14}|{'MENIT':^14}|")
print(f"|{umur_hari.days:^14}|{umur_jam:^14}|{umur_menit:^14}|")
line()

title("By Yasir")
line()