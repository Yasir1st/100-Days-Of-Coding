angka = 1
password = "yasir"
while angka < 4:
    angka += 1
    input_password = input("Masukkan Password : ")
    if(input_password == password):
        print("Berhasil Login")
        break
    else:
        print("Password Salah \n")

    if(angka == 4):
        print("Gagal Login")
        break

        