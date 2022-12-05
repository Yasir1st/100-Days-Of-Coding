from line import * # tidak disarankan menggunakan *
import packageMatematika

garis()
title("Manggunakan Init")
garis()

alas = int(input("Alas \t= "))
tinggi = int(input("Tinggi \t= "))
sisiMiring = packageMatematika.pythagoras.pythagoras_sisiMiring(alas,tinggi)
print(f"Sisi miring dari segitigas siku-siku jika alas = {alas} cm dan tinggi = {tinggi} cm adalah {sisiMiring} cm")
garis()

a = int(input("Nilai a \t= "))
b = int(input("Nilai b \t= "))
c = int(input("Nilai c \t= "))
hasil = packageMatematika.rumusABC.abc.a_b_c(a,b,c)
print(f"Jika a = {a}, b = {b}, dan c = {c} maka, {hasil}")
garis()