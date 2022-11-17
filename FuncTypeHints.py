'''Type Hints In Function'''
# Type Hint disini Berfungsi Untuk Mengatur tipe data parameter dan tipe data pada return function

# Bentuk Umum Function


def say_hi(nama):
    '''Say Hi Function'''
    say = print(f"Hello {nama}, you are so handsome :)")
    return (say)


# Jika seperti ini kita bebas mengisikan value dengan tipe data apa saja
say_hi("Yasir")
say_hi(2)       # dan pada saat pemanggilan function di hover
say_hi(True)

# Function With Hints


def ganjil(angka: int):
    '''Function Ganjil'''
    print(f"{angka} merupakan bilangan ganjil.")


ganjil(1)      # :int di atas berfungsi untuk memberikan pesan pada user pada saat meng hover fungsi bahwa parameter dari fungsi bertipe data int
ganjil("yasir")# Namun kita masih bisa mengisi value dengan tipe data apa saja pada fungsi

# Function With Hints and Output Return
# -> int disini berfungsi untuk mengatur value atau return dari fungsi yang kita buat
def sepuluh_pangkat(angkaa:int) -> int:
    '''Fungsi Dengan Hint Argument and Return'''
    pangkat = print(10**angkaa)
    return pangkat

sepuluh_pangkat(2) # Jika kita meng hover pada fungsi maka akan menampilkan tipe data apa yang menjadi return nilai dari fungsi 
                    # Ditandai dengan tanda -> (nama Variabel)
# sepuluh_pangkat("yasir") , jika kita mengisi value dengan tipe data yang berbeda pada fungsi maka akan terjadi error pada saat program di jalankan

# Hint String
import string  # Jika menggunakan string sebagai hint maka harus di import terlebih dahulu
def dontTouch(barang:string):
    '''Dont Touch Function'''
    print(f"Dont touch my {barang}")

dontTouch("Phone")

# Jika menggunakan Float dan Bolean caranya sama saja dengan Int
# :float, -> float
# :bool, -> bool