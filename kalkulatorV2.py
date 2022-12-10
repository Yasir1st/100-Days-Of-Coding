import os
os.system("cls")
import tkinter as tk
from tkinter.ttk import Label,Entry,Button


# Main window 
window = tk.Tk()
window.title("Kalkulator")
lebar = 500
tinggi = 500

# Mancari ukuran layar
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

# Membuat window muncul di tengah
centerx = int((screenWidth/2)-(lebar/2))
centery = int((screenHeight/2)-(tinggi/2))

window.geometry(f"{lebar}x{tinggi}+{centerx}+{centery}")

# Mengganti warna window
window.configure(bg="lightskyblue")

# Input Frame
input_frame =  tk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Variabel Dan Fungsi
ANGKA_PERTAMA = tk.IntVar()
ANGKA_KEDUA = tk.IntVar()

def tambah():
    hasil = ANGKA_PERTAMA.get() + ANGKA_KEDUA.get()
    hasil_tambah = Label(input_frame,text=f"Hasil Tambah = {hasil}")
    hasil_tambah.pack(padx=10,pady=10,fill="x",expand=True)
    return hasil_tambah

def kurang():
    hasil = ANGKA_PERTAMA.get() - ANGKA_KEDUA.get()
    hasil_tambah = Label(input_frame,text=f"Hasil Tambah = {hasil}")
    hasil_tambah.pack(padx=10,pady=10,fill="x",expand=True)
    return hasil_tambah

def kali():
    hasil = ANGKA_PERTAMA.get() * ANGKA_KEDUA.get()
    hasil_tambah = Label(input_frame,text=f"Hasil Tambah = {hasil}")
    hasil_tambah.pack(padx=10,pady=10,fill="x",expand=True)
    return hasil_tambah

def bagi():
    hasil = ANGKA_PERTAMA.get() / ANGKA_KEDUA.get()
    hasil_tambah = Label(input_frame,text=f"Hasil Tambah = {hasil}")
    hasil_tambah.pack(padx=10,pady=10,fill="x",expand=True)
    return hasil_tambah

# Menu
firts_angka = Label(input_frame,text="Angak Pertama : ")
firts_angka.pack(padx=10,pady=10,fill="x",expand=True)

firts_entry = Entry(input_frame,textvariable=ANGKA_PERTAMA)
firts_entry.pack(padx=10,pady=10,fill="x",expand=True)

second_angka = Label(input_frame,text="Angak Kedua : ")
second_angka.pack(padx=10,pady=10,fill="x",expand=True)

second_entry = Entry(input_frame,textvariable=ANGKA_KEDUA)
second_entry.pack(padx=10,pady=10,fill="x",expand=True)

button_tambah = Button(input_frame,text="TAMBAH",command=tambah)
button_tambah.pack(padx=10,pady=10,fill="x",expand=True)

button_kurang = Button(input_frame,text="KURANG",command=kurang)
button_kurang.pack(padx=10,pady=10,fill="x",expand=True)

button_kali = Button(input_frame,text="KALI",command=kali)
button_kali.pack(padx=10,pady=10,fill="x",expand=True)

button_bagi = Button(input_frame,text="BAGI",command=bagi)
button_bagi.pack(padx=10,pady=10,fill="x",expand=True)
# Main Loop
window.mainloop()