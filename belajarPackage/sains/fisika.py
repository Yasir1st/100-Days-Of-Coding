'''Module Fisika'''

def kecepatan(jarak,waktu):
    '''Kecepatan'''
    hasil = jarak/waktu
    return hasil

def jarak(kecepatan,waktu):
    '''Jarak'''
    hasil = kecepatan*waktu
    return hasil

def waktu(kecepatan,jarak):
    '''Waktu'''
    hasil = jarak/kecepatan
    return hasil

print(kecepatan(12,1))