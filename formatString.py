## format string

# string
nama = "Jisoo"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 7263.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 12
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 7400000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.1f}"
print(format_str)

# menampilkan leading zero
angka = 2012.576421
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.01010
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 3

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 169
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)