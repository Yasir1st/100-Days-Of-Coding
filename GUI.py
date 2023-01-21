# GUI => Graphical User Interface 
import os
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label,Entry,Button
from tkinter.messagebox import showinfo

os.system("cls")

# Main Window
window = tk.Tk()
window.configure(bg="chartreuse")
window.geometry("600x300")
window.resizable(False,False)
window.title("SAY App")

# Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''Tombol Click'''
    pesan = f"Why {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} Ganteng Buangedd ???"
    showinfo(title="Alert",message=pesan)
    messege_label = Label(input_frame,text=pesan)
    messege_label.pack(padx=10,pady=20,fill="x",expand=True)

# Frame Input
input_frame = ttk.Frame(window)
# Penempatan Grid or Pack or Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen Komponen
# Label Nama Depan
nama_depan_label = Label(input_frame,text="Nama Depan : ")
nama_depan_label.pack(padx=10,pady=10,fill="x",expand=True)
# Entry Nama Depan
nama_depan_entry = Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# Label Nama Belakang
nama_belakang_label = Label(input_frame,text="Nama Belakang : ")
nama_belakang_label.pack(padx=10,pady=10,fill="x",expand=True)
# Entry Nama Belakang
nama_belakang_entry = Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# BUTTON SUBMIT
button_kirim = Button(input_frame,text="Kirim",command=tombol_click)
button_kirim.pack(padx=10,pady=10,fill="x",expand=True)

# Main Loop => Berfungsi agar aplikasi yang dijalankan terus berjalan 
# sebelum di tutup oleh user
window.mainloop()