import datetime as dt

# Multi Keys/ dalam 1 dictionary boleh berisi data dengan berbagai tipe data yang berbeda
mahasiswa1 = {
	'nama':'Muhammad yasir',
	'nim':'D0222345',
	'sks_lulus':0,
	'beasiswa':False,
	'lahir':dt.datetime(2003,5,1)
}

mahasiswa2 = {
	'nama':'S. Firmansyah A',
	'nim':'D0222455',
	'sks_lulus':0,
	'beasiswa':False,
	'lahir':dt.datetime(2001,12,10)
}

mahasiswa3 = {
	'nama':'Sulkifli',
	'nim':'D0222340',
	'sks_lulus':0,
	'beasiswa':False,
	'lahir':dt.datetime(2003,2,27)
}

data_mahasiswa = {
	'MAH001':mahasiswa1,
	'MAH002':mahasiswa2,
	'MAH003':mahasiswa3
}

# pada format String tanda '<' berarti rata kiri, tanda '>' berarti rata kanan dan tanda '^' berarti rata tengah
print("-"*54)
print(f"{'NIM':<10} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*54)

for mahasiswa in data_mahasiswa:
	KEY = mahasiswa

	NAMA = data_mahasiswa[KEY]['nama']
	NIM = data_mahasiswa[KEY]['nim']
	SKS = data_mahasiswa[KEY]['sks_lulus']
	BEASISWA = data_mahasiswa[KEY]['beasiswa']
	LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

	print(f"{NIM:<10} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

print("-"*54)