total_belanja = int(input("Nilai total belanja(Rp): "))

if(total_belanja > 100000):
    diskon = total_belanja*10/100
    total_belanja_setelah_diskon = total_belanja-diskon
    print("Diskon(Rp): ",diskon)
    print("Nilai total setelah diskon(Rp): ",total_belanja_setelah_diskon)
elif(total_belanja <= 100000):
    print("Diskon(Rp): 0")
    print("Nilai total setelah diskon(Rp): ",total_belanja)