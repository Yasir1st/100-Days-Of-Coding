# Modul Mtk

def tambah(*args):
    '''Tambah'''
    hasil = 0
    for data in args:
        hasil += data
    
    return hasil

def kali(*args):
    '''Kali'''
    hasil = 1
    for data in args:
        hasil *= data
    
    return hasil

def pangkat(n:int):
    '''pangkat'''
    return lambda angka:angka**n