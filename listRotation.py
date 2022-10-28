def line():
    print("="*50)

line()
print("Input List".center(50))
line()
list_angka = [i for i in range(1,11) if i % 2 == 0]
print("List Sebelum Di Rotasi :")
print(list_angka)

list_angka.append(list_angka[0])
list_angka.pop(0)
print("List Setelah Di Rotasi :")
print(list_angka)
line()
