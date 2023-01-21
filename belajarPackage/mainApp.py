import sains.matematika
import sains.fisika
from sains import fisika
from sains.fisika import waktu as time
from line import garis,title

garis()
title("Matematika")
garis()

luasSegitiga = sains.matematika.luasSagitiga(12,5)
print(f"Luas Segitiga \t\t= {luasSegitiga:.0f} Cm")

luasJajargenjang = sains.matematika.luasJajargenjang(12,5)
print(f"Luas Jajarganjang \t= {luasJajargenjang} Cm")

garis()
title("Fisika")
garis()

kecepatan = sains.fisika.kecepatan(60,2)
print(f"Kecepatan \t\t= {kecepatan} Km/Jam")

jarak = fisika.jarak(60,2)
print(f"Jarak \t\t\t= {jarak} km")

waktu = time(30,60)
print(f"Waktu \t\t\t= {waktu} Jam")
garis()