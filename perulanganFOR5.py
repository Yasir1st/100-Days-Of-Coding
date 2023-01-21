# s = ''
# for i in range(20,0,-1):
#     s += str(i)+' '
#     print(s)

# total = 0
# proses = ''
# batas = int(input("Masukkan Batas Angka : "))

# for i in range(1,batas+1):
#     total += i

#     if(i == 1):
#         proses += "1"
#     else:
#         s = "+"+str(i)
#         proses += s

# print(f"{proses} = {total}")

listGanjil = []
listGenap = []

batas = int(input("Masukkan Batas : "))

for i in range(2, batas+1):
    if (i % 2 != 0):
        listGanjil.append(i)
    else:
        listGenap.append(i)


print("Ganjil", len(listGanjil))
print(listGanjil)
print("Genap", len(listGenap))
print(listGenap)
