# Function Args

def line():
    '''Line'''
    print("="*30)

line()
print("Function Args".center(30))

# Contoh 1
def judged(*args):
    '''Function Judged'''
    name = args[0]
    voice = args[1]
    look = args[2]
    hate = print(f"{name}, You're voice so {voice} and you look so {look}")
    return hate

line()
judged("Vanny","bad","bored")
line()

# Contoh 2 *args bisa diganti dengan kata apapun misalkan *angka
def tambah(*angka):
    '''Function Tambah'''
    output = 0
    for number in angka:
        output += number
    return output

hasil = tambah(1,2,3,4,5,6,9)
print(f"hasil = {hasil}")
line()