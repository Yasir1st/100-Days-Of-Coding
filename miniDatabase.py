# program list Makanan Khas
def line():
    print(30*"-")
list_makananKhas = []
line()
while True:
	print("\nMasukan Data Makanan")
	makanan = input("Nama Makanan\t: ")
	provinsi = input("Provinsi\t: ")

	foodAndPlaces = [makanan,provinsi]
	list_makananKhas.append(foodAndPlaces)

	print("\n","="*10,"Data Makanan","="*10)
	for index,food in enumerate(list_makananKhas):
		print(f"{index+1} | {food[0]} | {food[1]}")
	line()
	isLanjut = input("\nApakah dilanjutkan?(y/n)")

	if isLanjut == "n":
		break
print("PROGRAM SELESAI")
line()